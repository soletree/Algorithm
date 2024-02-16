with find_max as (
    select max(price) as price, category
    from food_product
    group by category
)

select category, price, product_name from food_product as food
where category in ('과자', '국', '김치', '식용유')
and (food.price, category) in (select price, category from find_max)
group by category
order by price desc;