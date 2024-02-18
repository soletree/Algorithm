SELECT 
u.user_id, u.nickname,
concat(city,' ',street_address1, ' ', street_address2),
concat(substring(tlno, 1, 3), '-',
       substring(tlno, 4, 4), '-',
       substring(tlno, 8, 4))
from used_goods_board b join used_goods_user u
on b.writer_id = u.user_id
group by b.writer_id
having count(b.writer_id) >= 3
order by 1 desc