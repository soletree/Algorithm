SELECT animal_id, animal_type, name
from animal_outs
where animal_id in (select animal_id 
                       from animal_ins 
                       where sex_upon_intake like "%Intact%")
and (sex_upon_outcome like "%Spayed%" or sex_upon_outcome like "%Neutered%")
order by 1 asc