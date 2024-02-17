SELECT board_id, writer_id, title, price,
if(status = 'SALE', '판매중', if(status = 'DONE', '거래완료', '예약중'))
from used_goods_board
where date_format(created_date, "%Y-%m-%d") = '2022-10-05'
order by board_id desc