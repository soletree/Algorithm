SELECT product_id, product_name, sum(price * amount)
from food_product p join food_order o using(product_id)
where date_format(produce_date, '%Y-%m') = '2022-05'
group by product_id
order by 3 desc, 1 asc