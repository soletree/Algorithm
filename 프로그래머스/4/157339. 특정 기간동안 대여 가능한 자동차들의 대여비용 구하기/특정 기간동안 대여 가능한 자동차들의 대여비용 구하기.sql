with plan as (
    select car_type,
    replace(duration_type, '일 이상', '') as duration,
    (100 - discount_rate) * 0.01 as rate
    from car_rental_company_discount_plan
    where (car_type = '세단' or car_type = 'SUV')
    and replace(duration_type, '일 이상', '') = '30'
), rental_car as (
    select *
    from car_rental_company_rental_history
    where date_format(start_date, '%Y-%m') <= '2022-11'
    and date_format(end_date, '%Y-%m-%d') >= '2022-11'
)

SELECT car_id, car_type, round(daily_fee * 30 * rate, 0) as fee
from car_rental_company_car c join plan p using(car_type)
where car_id not in (select car_id from rental_car)
and (daily_fee * 30 * rate) between 500000 and 1999999
order by 3 desc, 2 asc, 1 desc