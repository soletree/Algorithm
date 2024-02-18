with rare as (
    select item_id
    from item_info
    where rarity = 'RARE'
) 

select i.item_id, i.item_name, i.rarity
from item_info i join item_tree t
on i.item_id = t.item_id
where t.parent_item_id in (select item_id from rare)
order by 1 desc