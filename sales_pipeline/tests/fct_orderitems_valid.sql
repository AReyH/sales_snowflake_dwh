select
    *
from 
    {{ref('fct_orderitems')}}
where
    quantity < 0