# About Super Cashier
Super Cashier is a self-service supermarket cashier program that build with Python Language. This program have some feature, that will be explain below.

# Feature

1. Add item
    : you can add item, quantity and price per item
2. Update item
    1. Update item name
        : you can update the item name already entered
    2. Update item quantity
        : you can update the item quantiity already entered
    3. Update item price
        : you can update the item price already entered
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

All feature are compile in several menu, so customer can choose what feature they want use.

# Flowchart

![Flowchart](https://user-images.githubusercontent.com/128889408/230767415-1deb844b-ccd7-4770-bd95-ac5c1bddb6b2.png)


# Function

1. `add_item(name, quantity, price)`

    | Parameter name | Description | Data Type |
    | ----------- | ----------- | ----------- |
    | name | name of item | string |
    | quantity | quantity of item | number |
    | price | price of one item | number |
    
2. update_item
    1. `update_item_name(name, new_name)`
    
        | Parameter name | Description | Data Type |
        | ----------- | ----------- | ----------- |
        | name | name of item | string |
        | new_name | new name of item | string |
    
    2. `update_item_quantity(name, new_quantity)`
    
        | Parameter name | Description | Data Type |
        | ----------- | ----------- | ----------- |
        | name | name of item | string |
        | new_quantity | new quantity of item | number |
    
    3. `update_item_price(name, new_price)`
    
        | Parameter name | Description | Data Type |
        | ----------- | ----------- | ----------- |
        | name | name of item | string |
        | new_price | new price of item | number |
    
3. delete item
    1. `delete_item(name)`
    2. `reset_transaction()`
4. `check_order()`
5. `total_price()`

If user input non numeric into item_quantity or item_price, system will be send an error message

# How to Use

1.	Download all Python file/module into one local directory
2.	Open terminal and go to local directory where file has been download exists
3.	Running Cashier.py
    ``` 
    python Cashier.py 
    ```

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

    ![image](https://user-images.githubusercontent.com/128889408/230767622-c8b575d7-f385-49bf-a919-b804167b4c9c.png)

# Conclusion
1. In current program all purchased items are store in a dictionary
2. For next development all item already entered by customer can store into database
