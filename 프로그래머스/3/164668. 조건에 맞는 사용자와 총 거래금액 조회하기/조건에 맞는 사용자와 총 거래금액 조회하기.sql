with done as (
    select *
    from used_goods_board
    where status = 'DONE'
), total as (
    select writer_id, sum(price) as total
    from done
    group by writer_id
    having total >= 700000
)

select user.user_id, user.nickname, total.total
from total inner join used_goods_user as user
on total.writer_id = user.user_id
order by total.total asc;