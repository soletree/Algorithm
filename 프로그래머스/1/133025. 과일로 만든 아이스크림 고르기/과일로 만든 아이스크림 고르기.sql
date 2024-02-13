SELECT a.flavor
from first_half as a inner join icecream_info as b
on a.flavor = b.flavor
where total_order > 3000
and ingredient_type = 'fruit_based'
order by total_order desc;