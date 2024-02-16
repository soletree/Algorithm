with rental_list as (
    select car_id, end_date
    from car_rental_company_rental_history
    where date_format(end_date, "%Y-%m-%d") >= '2022-10-16' 
    and date_format(start_date, "%Y-%m-%d") <= '2022-10-16'
)

SELECT car_id, 
if(car_id in (select car_id from rental_list), "대여중", "대여 가능") as AVAILABILITY
from car_rental_company_rental_history
group by car_id
order by car_id desc;