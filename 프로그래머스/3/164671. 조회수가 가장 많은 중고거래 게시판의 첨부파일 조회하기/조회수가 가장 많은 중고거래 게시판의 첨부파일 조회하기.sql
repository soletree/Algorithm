with most as (
    select board_id
    from used_goods_board
    order by views desc
    limit 1
)

SELECT
concat('/home/grep/src/', f.board_id, '/', f.file_id, file_name, f.file_ext) 
as FILE_PATH
from used_goods_file f
where f.board_id in (select board_id from most)
order by f.file_id desc;