SELECT name, datetime
from animal_ins
where animal_id not in (select animal_id from animal_outs)
order by 2 asc
limit 3