with flavor_first as (
    select flavor, sum(total_order) as total
    from first_half
    group by flavor
), flavor_july as (
    select flavor, sum(total_order) as total
    from july
    group by flavor
)

SELECT flavor
from flavor_first f join flavor_july j using(flavor)
group by flavor
order by sum(f.total + j.total) desc
limit 3