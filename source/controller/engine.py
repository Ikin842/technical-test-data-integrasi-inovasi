import pandas as pd
import typer
import time
from loguru import logger
from service import postgres_svc

app = typer.Typer()

@app.command()
def run():
    AutoIngest().main()

class AutoIngest:
    def __init__(self):
        self.postgres = postgres_svc
        self.table_name = "retail_kita_analytic"

    @staticmethod
    def transform(transactions, products, customers):
        transactions['timestamp'] = pd.to_datetime(transactions['timestamp'], errors='coerce')
        transactions['quantity'] = transactions['quantity'].fillna(0).astype(int)

        df = transactions.merge(products, on="product_id", how="left")
        df = df.merge(customers, on="customer_id", how="left")

        df['total_price'] = df['quantity'] * df['price']
        df['year'] = df['timestamp'].dt.year
        df['month'] = df['timestamp'].dt.month
        df['day'] = df['timestamp'].dt.day
        df['weekday'] = df['timestamp'].dt.day_name()
        df['week_number'] = df['timestamp'].dt.isocalendar().week

        df['is_high_value_product'] = (df['price'] > 1_000_000).astype(bool)
        df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')
        df['customer_tenure_days'] = (df['timestamp'] - df['join_date']).dt.days
        df['is_new_customer'] = (df['customer_tenure_days'] <= 30).astype(bool)

        df['basket_size'] = df['quantity']
        df['revenue_band'] = pd.cut(
            df['total_price'], bins=[-1, 500000, 2000000, float('inf')], labels=['Low', 'Medium', 'High']
        )
        df = df.drop_duplicates(subset=['transaction_id'])
        return df

    def main(self):
        transactions = pd.read_csv("resources/transactions.csv")
        products = pd.read_csv("resources/products.csv")
        customers = pd.read_csv("resources/customers.csv")

        start_time = time.time()
        self.postgres.connect()
        df = self.transform(
            transactions, products, customers
        )

        count = self.postgres.ingest(df, table_name=self.table_name)
        if count:
            logger.info("===============================")
            logger.info("end time : {}", time.time() - start_time)
            logger.info("===============================")
            logger.info("Ingested {}: {}", self.table_name, count)

if __name__ == "__main__":
    app()
