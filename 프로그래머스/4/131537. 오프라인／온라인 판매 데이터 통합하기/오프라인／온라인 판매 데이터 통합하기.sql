with online_ as (
    select * 
    from online_sale 
    where date_format(sales_date, "%Y-%m") = '2022-03'
), offline_ as (
    select * 
    from offline_sale 
    where date_format(sales_date, "%Y-%m") = '2022-03'
)

SELECT date_format(sales_date, "%Y-%m-%d") as date,
product_id, user_id, sales_amount
from online_
union
SELECT date_format(sales_date, "%Y-%m-%d") as date,
product_id, NULL, sales_amount
from offline_
order by date, product_id, user_id asc