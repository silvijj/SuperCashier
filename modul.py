"""
This module is built for support the self-service cashier of supermarket program ,consist of several functions:
  add_item,
  update item
  delete item
  reset item
  calculate transaction (all item)
"""

# library list
from tabulate import tabulate

class Transaction:
  """
  A class to represent a transaction
  Attribute: name (string)
  """
  # dictionary to hold data items 
  dct = {}

  # dictionary of rule to get discount
  discount = {
      500_000 : 10,
      300_000 : 8,
      200_000 : 5,
  }

  def __init__(self, name):
    """
    Constructs all necessary attributes for transaction object
    Parameter: name represent customer name
    """
    self.name = name

  def add_item(self,item_name, quantity, price):
    """
    Function for add item
    Parameter: item name (string), quantity (int), price (int)
    """
    self.dct.update({item_name:[quantity,price]})
  
  def update_item_name(self,item_name,new_item_name):
    """
    Function for update item name
    Parameter: item name (string), new item name (string)
    """
    self.dct[new_item_name] = self.dct[item_name]
    del self.dct[item_name]

  def update_quantity(self,item_name,new_quantity):
    """
    Function for update item quantity
    Parameter: item name (string), new item quantity (string)
    """
    self.dct[item_name].insert(0,new_quantity)
    self.dct[item_name].pop(1)

  def update_price(self,item_name,new_price):
    """
    Function for update item price
    Parameter: item name (string), new item price (string)
    """
    self.dct[item_name].insert(1,new_price)
    self.dct[item_name].pop(2)
    
  def delete_item(self,item_name):
    """
    Function for delete one item
    Parameter: item name that will be delete
    """
    self.dct.pop(item_name)

  def reset_transaction(self):
    """
    Function for delete all item
    Parameter: none
    """
    self.dct.clear()

  def check_order(self):
    """
    Function for check all items alreadu entered in tabular form
    Parameter: none
    """
    no = 0
    print_list = []

    for k, v in self.dct.items():
      no += 1
      quantity = v[0]
      price = v[1]
      amount = quantity * price
      add_list = [no,k,quantity,price,amount]
      print_list.append(add_list)

    print(tabulate(print_list, headers=['No','Nama Item','Jumlah Item','Harga/Item','Total Item'], tablefmt="github"))

  def total_price(self):
    """
    Function for summary all item (total amount, total quantity, discount, payment total)
    Parameter: none
    """
    total_amount = 0
    total_quantity = 0
    get_discount = 0

    for value in self.dct:
      amount = self.dct[value][0] * self.dct[value][1]
      quantity = self.dct[value][0]
      total_amount = total_amount + amount
      total_quantity = total_quantity + quantity
    
    for val in self.discount:
      if total_amount > val:
        get_discount = self.discount[val]
        break

    discount_amount = total_amount * get_discount/100
    payment_total = total_amount - discount_amount
    
    summary = [
        ['Total belanja',f'Rp. {total_amount:,.2f}'],
        ['Jumlah item',f'{total_quantity}'],
        ['Diskon',f'{get_discount} %'],
        ['Potongan harga',f'Rp. {discount_amount:,.2f}']
    ]

    print(tabulate(summary, tablefmt="plain"))
    print('')
    print(f"Total belanja yang harus dibayar adalah Rp. {payment_total:,.2f}")

  def __str__(self):
    """Function for get all items already entered"""
    return f'Item yang dibeli {self.name} adalah: {self.dct}'