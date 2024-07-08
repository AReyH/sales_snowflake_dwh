select
    sale_id as order_id,
    customer_id,
    date as order_date,
    total_amount
from
    {{ref('stg_sales')}} as stg_sales
order by
    order_date