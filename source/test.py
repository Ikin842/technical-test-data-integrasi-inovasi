from service import postgres_svc

query = """
WITH datas AS (
    SELECT
        year,
        month,
        SUM(total_price) AS monthly_revenue
    FROM retail_kita_analytic
    GROUP BY year, month
)
SELECT *
FROM datas
ORDER BY year, month;

"""

postgres_svc.connect()

result = postgres_svc.read_query(query)
print(result)