with best as (
    select member_id, 
    dense_rank() over (order by count(*) desc) as write_rank
    from rest_review
    group by member_id
)

SELECT member_name, review_text, date_format(review_date, "%Y-%m-%d")
from rest_review join member_profile using(member_id)
where member_id in (select member_id from best
                    where write_rank = 1)
order by 3, 2 asc