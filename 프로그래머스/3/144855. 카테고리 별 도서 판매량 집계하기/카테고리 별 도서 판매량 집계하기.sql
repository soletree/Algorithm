SELECT a.category, sum(sales) as total_sales from book as a 
inner join book_sales as b
on a.book_id = b.book_id
where date_format(sales_date, "%Y-%m") = '2022-01'
group by category
order by category asc;
