with joined as (
    select user_id
    from user_info
    where year(joined) = 2021
), joined_cnt as (
    select count(*) as cnt
    from joined
), joined_sale as (
    select * 
    from online_sale join user_info using(user_id)
    where user_id in (select user_id from joined)
)

select year(sales_date) as year,
month(sales_date) as month,
count(distinct user_id), 
round(count(distinct user_id)/(select count(*) from joined), 1)
from joined_sale
group by 1, 2
order by 1, 2 asc