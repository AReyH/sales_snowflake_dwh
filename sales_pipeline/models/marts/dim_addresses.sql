select
    customer_id,
    address,
    city,
    state,
    postal_code
from 
    {{ ref('stg_sales')}} as stg_sales
