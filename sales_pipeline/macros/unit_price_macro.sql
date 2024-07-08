{% macro unit_price(total_amount,quantity) %}
    ({{total_amount}} / {{quantity}})::int
{% endmacro %}