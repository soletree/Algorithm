SELECT ins.animal_id, ins.name
from animal_ins as ins inner join animal_outs as outs
on ins.animal_id = outs.animal_id
order by datediff(outs.datetime, ins.datetime) desc
limit 2;