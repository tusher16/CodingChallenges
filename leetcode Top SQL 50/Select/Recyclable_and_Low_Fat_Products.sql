with prod_tab as (
    select product_id
    from Products
    where low_fats = 'Y' and recyclable = 'Y'
)

Select product_id
from prod_tab 