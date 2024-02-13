SELECT 
title as TITLE,
used_goods_board.board_id as BOARD_ID,
reply_id as REPLY_ID,
used_goods_reply.writer_id as WRITER_ID,
used_goods_reply.contents as CONTENTS,
date_format(used_goods_reply.created_date, "%Y-%m-%d") as CREATED_DATE
from used_goods_board inner join used_goods_reply
on used_goods_board.board_id = used_goods_reply.board_id
where date_format(used_goods_board.created_date, "%Y-%m") = "2022-10"
order by used_goods_reply.created_date asc, 
title asc;