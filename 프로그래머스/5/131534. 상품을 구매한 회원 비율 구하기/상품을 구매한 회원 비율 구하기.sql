with joined as (
    select user_id
    from user_info 
    where year(joined) = 2021
)


SELECT year(sales_date),
month(sales_date),
count(distinct user_id), 
round(count(distinct user_id) / (select count(*) from joined), 1)
from online_sale
where user_id in (select user_id from joined)
group by 1, 2
order by 1 asc, 2 asc