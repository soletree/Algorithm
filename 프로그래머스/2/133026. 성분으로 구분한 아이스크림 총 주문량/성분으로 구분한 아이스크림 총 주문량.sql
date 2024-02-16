SELECT b.ingredient_type as type, sum(a.total_order) as TOTAL_ORDER
from first_half as a inner join icecream_info as b
on a.flavor = b.flavor
group by type
order by TOTAL_ORDER asc;