# sales_snowflake_dwh

```SQL
use warehouse dbt_wh;

use role accountadmin;

create warehouse dbt_wh with warehouse_size = 'x-small';
create database if not exists sales;
create role if not exists dbt_role;

show grants on warehouse dbt_wh;

grant usage on warehouse dbt_wh to role dbt_role;
grant role dbt_role to user USER_NAME;
grant all on database dbt_db to role dbt_role;

use role dbt_role;

create schema sales.mock;

create schema sales.raw;
```

I created the mock data running [`data.py`](src/data.py). This output the `sales .csv` file. I uploaded this file into Snowflake and loaded it into the schema sales.raw.

