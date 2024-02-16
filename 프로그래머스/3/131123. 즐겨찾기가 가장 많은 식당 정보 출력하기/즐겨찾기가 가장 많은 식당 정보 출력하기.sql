with most_favorite as (
    select food_type, max(favorites) as maximum
    from rest_info
    group by food_type
)

select a.food_type, a.rest_id, a.rest_name, a.favorites  from rest_info as a 
inner join most_favorite as b 
on a.food_type = b.food_type
where a.favorites = b.maximum
order by a.food_type desc;