with best as (
    select member_id, count(*) as cnt
    from rest_review
    group by member_id
    order by 2 desc
    limit 1
)

SELECT member_name, review_text, date_format(review_date, "%Y-%m-%d")
from rest_review join member_profile using(member_id)
where member_id in (select member_id from best)
order by 3, 2 asc