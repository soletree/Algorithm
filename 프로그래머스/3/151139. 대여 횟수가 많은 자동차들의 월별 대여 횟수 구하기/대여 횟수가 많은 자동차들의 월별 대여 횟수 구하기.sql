with date_table as (
    select car_id
    from car_rental_company_rental_history
    where date_format(start_date, "%Y") = 2022 
    and date_format(start_date, "%m") between 8 and 10
    group by car_id
    having count(*) >= 5
)

SELECT date_format(start_date, "%m") as month, car_id, 
count(*) as RECORDS
from car_rental_company_rental_history
where date_format(start_date, "%Y") = 2022 
and date_format(start_date, "%m") between 8 and 10
and car_id in (select car_id from date_table)
group by month, car_id
order by month asc, 
car_id desc;