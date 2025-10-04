-- name: top_products
-- Produk Terlaris: 5 produk dengan pendapatan tertinggi
WITH datas AS (
    SELECT
        product_id,
        product_name,
        SUM(total_price) AS total_revenue
    FROM retail_kita_analytic
    GROUP BY product_id, product_name
)
SELECT *
FROM datas
ORDER BY total_revenue DESC
LIMIT 5;


-- name: top_customers
-- Pelanggan paling berharga: 10 pelanggan dengan pengeluaran tertinggi
WITH datas AS (
    SELECT
        customer_id,
        customer_location,
        SUM(total_price) AS total_spent
    FROM retail_kita_analytic
    GROUP BY customer_id, customer_location
)
SELECT *
FROM datas
ORDER BY total_spent DESC
LIMIT 10;


-- name: monthly_revenue
-- Tren Penjualan Bulanan
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
