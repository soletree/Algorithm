with seoul as (
    select rest_id 
    from rest_info 
    where address like "서울%"
)

SELECT rest_id, rest_name, food_type, favorites, address,
round(avg(review_score), 2)
from rest_info join rest_review using(rest_id)
where rest_id in (select rest_id from seoul)
group by rest_id
order by 6 desc, 4 desc