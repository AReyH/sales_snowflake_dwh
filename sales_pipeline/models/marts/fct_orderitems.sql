select
    {{
    dbt_utils.generate_surrogate_key([
        'sale_id',
        'product_id'
    ])
    }} as order_item_id,
    sale_id as order_id,
    product_id,
    quantity,
    {{ unit_price('stg_sales.total_amount','stg_sales.quantity') }} as unitprice
from
    {{ref('stg_sales')}} as stg_sales
