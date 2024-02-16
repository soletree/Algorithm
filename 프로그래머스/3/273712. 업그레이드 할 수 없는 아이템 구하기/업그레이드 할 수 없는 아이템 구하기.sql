with upgrades as (
    select item_id
    from item_tree
    where item_id in (select parent_item_id 
                      from item_tree)
)

select item_id, item_name, rarity  
from item_info 
where item_id not in (select item_id from upgrades)
order by item_id desc; 