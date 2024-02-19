with plan as (
    select car_id, daily_fee, 
    replace(duration_type, '일 이상', '') as duration_type,
    (100 - discount_rate) * 0.01 as rate
    from car_rental_company_car join 
    car_rental_company_discount_plan using(car_type)
    where car_type = '트럭'
    union
    select car_id, daily_fee,
    0 as duration_type, 1 as rate
    from car_rental_company_car 
    where car_type = '트럭' 
)
select history_id,
round(daily_fee * (datediff(end_date, start_date)+1) * rate, 0) as fee
from car_rental_company_rental_history join plan using(car_id)
where 
case 
 when datediff(end_date, start_date)+1 < 7 then 0
 when datediff(end_date, start_date)+1 between 7 and 29 then 7
 when datediff(end_date, start_date)+1 between 30 and 89 then 30
 when datediff(end_date, start_date)+1 >= 90 then 90
end = duration_type
order by 2 desc, 1 desc