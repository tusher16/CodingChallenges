# [Recyclable and Low Fat Products Finder](https://leetcode.com/problems/recyclable-and-low-fat-products/description/?envType=study-plan-v2&envId=top-sql-50)

This readme provides a solution to find product IDs that are both low fat and recyclable.

## Table Schema

### `Products`

| Column Name | Type    |
|-------------|---------|
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |

- `product_id` is the primary key.
- `low_fats` is an ENUM of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
- `recyclable` is an ENUM of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.

## Solution

The solution is written in SQL and finds the product IDs of items that are both low fat and recyclable.

SQL:
```sql
with prod_tab as (
    select product_id
    from Products
    where low_fats = 'Y' and recyclable = 'Y'
)

Select product_id
from prod_tab 
```

## Usage

To use this solution, run the above SQL on your preferred database management system that contains the `Products` table. The output will list product IDs that match the criteria.
