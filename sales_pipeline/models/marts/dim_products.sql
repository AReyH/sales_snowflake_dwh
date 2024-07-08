select
    product_id,
    product_name,
    product_category,
    product_brand,
    product_price,
    product_description,
    product_stock_quantity,
    product_date_added

from
    {{ref('stg_sales')}} as stg_sales
order by
    product_date_added