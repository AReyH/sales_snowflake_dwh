select
    customer_id,
    first_name,
    last_name,
    email,
    phone_number,
    dob,
    gender,
    registration_date
from
    {{ ref('stg_sales')}} as stg_sales
order by
    registration_date

