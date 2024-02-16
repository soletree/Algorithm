with recursive number as (
    select 0 as n
    union all
    select n+1 from number where n < 23
), hour_list as (
    SELECT date_format(datetime, "%H") as hour, count(*) as cnt
    from animal_outs
    group by hour
)
select n.n, if(h.cnt is null, 0, h.cnt)
from hour_list as h right join number as n
on h.hour = n.n