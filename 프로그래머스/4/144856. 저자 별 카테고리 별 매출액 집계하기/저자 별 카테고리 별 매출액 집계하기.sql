with date as (
    select book_id as bid, sum(sales) as sales_cnt
    from book_sales 
    where date_format(sales_date, "%Y-%m") = "2022-01"
    group by book_id
), total as (
    select *
    from date inner join book
    on book.book_id = date.bid
)

SELECT 
author.author_id,
author.author_name,
total.category, 
sum(total.price * total.sales_cnt)
from total inner join author
on author.author_id = total.author_id
group by total.author_id, total.category
order by total.author_id asc,
total.category desc;