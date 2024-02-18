SELECT p.product_code, 
sum(p.price * o.sales_amount)
from product p join offline_sale o
on p.product_id = o.product_id
group by p.product_code
order by 2 desc, 1 asc