with doctor_appointment as (
    select d.dr_name, d.dr_id, d.mcdp_cd, 
    a.apnt_no, a.pt_no, a.apnt_ymd as ymd
    from doctor d join appointment a
    on d.dr_id = a.mddr_id
    where date_format(a.apnt_ymd, "%Y-%m-%d") = '2022-04-13'
    and a.apnt_cncl_yn = 'N'
    and d.mcdp_cd = 'CS'
)

SELECT apnt_no, pt_name, pt_no, mcdp_cd, dr_name, ymd
from doctor_appointment join patient using(pt_no)
order by 6 asc