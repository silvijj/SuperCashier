"""isi docstring ini"""

# daftar library

from tabulate import tabulate

class Transaction:
  dct = {}

  discount = {
      500_000 : 10,
      300_000 : 8,
      200_000 : 5,
  }

  def __init__(self, name):
    self.name = name

  def add_item(self,item_name, quantity, price):
    self.dct.update({item_name:[quantity,price]})
  
  def update_item_name(self,item_name,new_item_name):
    self.dct[new_item_name] = self.dct[item_name]
    del self.dct[item_name]

  def update_quantity(self,item_name,new_quantity):
    self.dct[item_name].insert(0,new_quantity)
    self.dct[item_name].pop(1)

  def update_price(self,item_name,new_price):
    self.dct[item_name].insert(1,new_price)
    self.dct[item_name].pop(2)
    
  def delete_item(self,item_name):
    self.dct.pop(item_name)

  def reset_transaction(self):
    self.dct.clear()

  def total_price(self):
    total = 0
    get_discount = 0

    for value in self.dct:
      amount = self.dct[value][0] * self.dct[value][1]
      total = total + amount
    
    for val in self.discount:
      if total > val:
        get_discount = self.discount[val]
        break

    discount_amount = total * get_discount/100
    payment_total = total - discount_amount
    
    summary = [
        ['Total belanja',f'Rp. {total:,.2f}'],
        ['Diskon',f'{get_discount} %'],
        ['Potongan harga',f'Rp. {discount_amount:,.2f}']
    ]

    print(tabulate(summary, tablefmt="plain"))
    print('')
    print(f"Total belanja yang harus dibayar adalah Rp. {payment_total:,.2f}")

  def check_order(self):
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

  def __str__(self):
    return f'Item yang dibeli {self.name} adalah: {self.dct}'