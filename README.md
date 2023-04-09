# About Super Cashier
Super Cashier is a cashier program that build with Python Language. This program have some feature, that will be explain below.

# Objektif

# Feature

1. Add item
    : you can add item, quantity and price per item
2. Update item
    1. Update item name
        : you can update the item name that has been input before
    2. Update item quantity
        : you can update the item quantiity that has been input before
    3. Update item price
        : you can update the item price that has been input before
3. Delete item
    1. Delete one item
    2. Delete all item / reset transaction
4. Check Order
      : Check for errors when entering the data and return message
5. Total Price
        : calculate total spending and get discount if meet the rule
    
    | Total Price | Discount |
    | ----------- | ----------- |
    | more than Rp 200.000 | 5% |
    | more than Rp 300.000 | 8% |
    | more than Rp 500.000 | 10% |

# Flowchart

# Function

1. `add_item(item_name, item_quantity, item_price)`

    | Parameter name | Description | Data Type |
    | ----------- | ----------- | ----------- |
    | item_name | name of item | string |
    | item_quantity | quantity of item | number |
    | item_price | price of one item | number |
2. update_item
    1. `update_item_name(item_name, new_item_name)`
    
        | Parameter name | Description | Data Type |
        | ----------- | ----------- | ----------- |
        | item_name | name of item | string |
        | new_item_name | new name of item | string |
    
    2. `update_item_quantity(item_name, new_item_quantity)`
    
        | Parameter name | Description | Data Type |
        | ----------- | ----------- | ----------- |
        | item_name | name of item | string |
        | new_item_quantity | new quantity of item | number |
    
    3. `update_item_price(item_name, new_item_price)`
    
        | Parameter name | Description | Data Type |
        | ----------- | ----------- | ----------- |
        | item_name | name of item | string |
        | new_item_price | new price of item | number |
    
3. delete item
    1. `delete_item(item_name)`
    2. `reset_transaction()`
4. `check_order()`
5. `total_price()`

# Demo
1. Add item 

    ![image](https://user-images.githubusercontent.com/128889408/230732773-373cdccf-8dce-415f-a676-b7f45fe0275f.png)

2. Update Item 

    ![image](https://user-images.githubusercontent.com/128889408/230751578-155d08ac-7062-4783-a107-a544bbea5749.png)

3. Delete item 

    ![image](https://user-images.githubusercontent.com/128889408/230732979-ee5aa8c1-6849-45f6-b92a-748f1fcab41e.png)

4. Reset Transaction 

    ![image](https://user-images.githubusercontent.com/128889408/230732948-1231fc7d-d9d8-406a-9c93-17e91ac9872e.png)

5. Check Order and Total Price

    ![image](https://user-images.githubusercontent.com/128889408/230733128-f7b408f8-d2fb-4f7d-9c7d-d2a16eb68274.png)

# Conclusion
