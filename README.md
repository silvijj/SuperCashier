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

![230767415-1deb844b-ccd7-4770-bd95-ac5c1bddb6b2 edit](https://user-images.githubusercontent.com/128889408/232315653-43f90cb1-5384-4136-b8e3-6b9758b5cd15.png)



# Code Description

1. cashier.py
    : are main file that will be run. Will be function as a file that running module already imported
2. module.py
    : are module file and consist of several function to support main file

## main.py
Consist of flow to running the program likes define on flowchart before. At this part there is error handling when input not meet the requierement, likes:
1. While user enter menu outside from list, system will send an error message
    ```
      try:
        menu = int(menu)
      except ValueError:
        print(f'Menu yang harus dimasukkan adalah angka 1-{len(list_menu)-1}!!!')
      else:
          if menu not in range(1, len(list_menu)):
            print('Menu yang anda masukkan tidak terdaftar!!!')
          elif menu in range(1, len(list_menu)-1):
            if menu == 1:
                ...
    ```
    
2. While user enter non numeric into item_quantity or item_price, system will be send an error message
    ```
                    elif menu_edit == 2:
                      new_quantity = input('Jumlah item baru\t: ')
                      try:
                        new_quantity = int(new_quantity)
                      except ValueError:
                        print(f'Jumlah item yang anda masukkan salah!!! nilai yang \
                        diterima adalah angka')
                      else:
                        trnsct_123.update_item_quantity(name, new_quantity)

                        ...
    ```

## module.py

1. `add_item(name, quantity, price)`

    | Parameter name | Description | Data Type |
    | ----------- | ----------- | ----------- |
    | name | name of item | string |
    | quantity | quantity of item | number |
    | price | price of one item | number |
    
    ```
      def add_item(self,name, quantity, price):
        """
        Function for add item
        Parameter: item name (string), quantity (int), price (int)
        """
        self.items.update({name:[quantity,price]})
    ```
    This function for add items with several variable likes on table above. If parameter already entered then items values will be insert into items dictionary.
    
2. update_item
    1. `update_item_name(name, new_name)`
    
        | Parameter name | Description | Data Type |
        | ----------- | ----------- | ----------- |
        | name | name of item | string |
        | new_name | new name of item | string |
        
        ```
          def update_item_name(self, name, new_name):
            """
            Function for update item name
            Parameter: item name (string), new item name (string)
            """
            self.items[new_name] = self.items[name]
            del self.items[name]
        ```
        This function for update item name with several variable likes on table above. If parameter already entered then item name will insert into items dictionary and the old one will be deleted.
    
    2. `update_item_quantity(name, new_quantity)`
    
        | Parameter name | Description | Data Type |
        | ----------- | ----------- | ----------- |
        | name | name of item | string |
        | new_quantity | new quantity of item | number |
        
        ```
          def update_item_quantity(self, name, new_quantity):
            """
            Function for update item quantity
            Parameter: item name (string), new item quantity (string)
            """
            self.items[name].insert(0,new_quantity)
            self.items[name].pop(1)
        ```
        This function for update item quantity with several variable likes on table above. If parameter already entered then item quantity will be insert into items dictionary on values part at index 0 and values at index 1 will be deleted.
    
    3. `update_item_price(name, new_price)`
    
        | Parameter name | Description | Data Type |
        | ----------- | ----------- | ----------- |
        | name | name of item | string |
        | new_price | new price of item | number |
        
       ``` 
           def update_item_price(self, name, new_price):
            """
            Function for update item price
            Parameter: item name (string), new item price (string)
            """
            self.items[name].insert(1,new_price)
            self.items[name].pop(2)
        ```
        This function for update item price with several variable likes on table above. If parameter already entered then item price will be insert into items dictionary on values part at index 1 and values at index 2 will be deleted.
    
3. delete item
    1. `delete_item(name)`
        Parameter: item name
        ```
          def delete_item(self, name):
            """
            Function for delete one item
            Parameter: item name that will be delete
            """
            self.items.pop(name)
        ```
        This function for delete specific item based on parameter already entered.
        
    2. `reset_transaction()`
        ```
          def reset_transaction(self):
            """
            Function for delete all item
            Parameter: none
            """
            self.items.clear()
        ```
        This function for clear all item on dictionary.
        
4. `check_order()`
    ```
        def check_order(self):
            """
            Function for check all items alreadu entered in tabular form
            Parameter: none
            """
            no = 0
            print_list = []
            headers = [
              'No',
              'Nama Item',
              'Jumlah Item',
              'Harga/Item',
              'Total Item'
            ]

            ...

            print(tabulate(print_list, headers = headers, tablefmt="github"))
    ```
    This function for check order already entered and show as a table. All values from dictionary items is entered into list items so we can show the sequence number int table. The table consist of sequence number, item name, quantity, price, total price per item.
    
5. `total_price()`
    
    ```
      def total_price(self):
        """
        Function for summary all item (total amount, total quantity, discount, 
        payment total)
        Parameter: none
        """
        total_amount = 0
        total_quantity = 0
        get_discount = 0

        for value in self.items:
          amount = self.items[value][0] * self.items[value][1]
          quantity = self.items[value][0]
          total_amount = total_amount + amount
          total_quantity = total_quantity + quantity

        for val in self.discount:
          if total_amount > val:
            get_discount = self.discount[val]
            break

        ...

        print(tabulate(summary, tablefmt="plain"))
        print('')
        print(f"Total belanja yang harus dibayar {self.customer_name} adalah Rp. \
        {payment_total:,.2f}") 
    ```
    This function for calculate all item already entered, calculate total purchase, calculate discount and calculate payment amount after discount. Discount reference are read from dictionary of discount


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
