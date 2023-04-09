from tabulate import tabulate
from modul import Transaction

list_menu = [
    ['Menu','Keterangan'],
    ['[1]','Tambah item'],
    ['[2]','Edit item'],
    ['[3]','Delete item'],
    ['[4]','Reset transaksi'],
    ['[5]','Hitung total belanja'],
    ['[6]','Selesai']
]

list_menu_edit = [
    ['Menu','Keterangan'],
    ['[1]','Edit nama item'],
    ['[2]','Edit jumlah item'],
    ['[3]','Edit harga/item'],
    ['[4]','Kembali ke menu utama']
]
        
customer_name = input('Nama Pembeli\t: ')
trnsct_123 = Transaction(customer_name)

print('')
print(tabulate(list_menu, headers = "firstrow"))
menu = input('\nPilih menu\t: ')
print('')

while True:
  try:
    menu = int(menu)
  except ValueError:
    print(f'Menu yang harus dimasukkan adalah angka 1-{len(list_menu)-1}!!!')
  else:
      if menu not in range(1, len(list_menu)):
        print('Menu yang anda masukkan tidak terdaftar!!!')
      elif menu in range(1, len(list_menu)-1):
        if menu == 1:
          tambah_item = 'y'
          while tambah_item == 'y':
            name = input('Nama Item\t: ')
            quantity = input('Jumlah Item \t: ')
            price = input('Harga/Item \t: ')

            try:
              quantity = int(quantity)
            except ValueError:
              print('Jumlah item yang anda masukkan salah!!! nilai yang \
              diterima adalah angka')
            else:
              try:
                price = int(price)
              except ValueError:
                print('Harga item yang anda masukkan salah!!! nilai yang \
                diterima adalah angka')
              else:
                trnsct_123.add_item(name, quantity, price)
                print('')
              
                tambah_item = input('Tambah item? [y/n]\t: ').lower()
                print('')

                if tambah_item == 'n':
                  break
                elif tambah_item not in ['y','n']:
                  print('Isi dengan y/n')
                  tambah_item = input('Tambah item? [y/n]\t: ').lower()
                  print('')

          print(trnsct_123)
        
        elif menu == 2:
          while menu == 2:
            print(tabulate(list_menu_edit, headers = "firstrow"))
            print('')
            menu_edit = input('Pilih menu\t: ')

            try:
              menu_edit = int(menu_edit)
            except ValueError:
              print(f'Menu yang harus dimasukkan adalah angka \
              1-{len(list_menu_edit)-1}!!!')
            else:
              if menu_edit not in range(1, len(list_menu_edit)):
                print('Menu yang anda masukkan tidak terdaftar!!!')
              elif menu_edit in range(1, len(list_menu_edit)-1):
                print('')
                name = input('Nama item\t: ')
                
                if menu_edit == 1:
                  new_name = input('Nama item baru\t: ')
                  trnsct_123.update_item_name(name, new_name)
                elif menu_edit == 2:
                  new_quantity = input('Jumlah item baru\t: ')
                  try:
                    new_quantity = int(new_quantity)
                  except ValueError:
                    print(f'Jumlah item yang anda masukkan salah!!! nilai yang \
                    diterima adalah angka')
                  else:
                    trnsct_123.update_item_quantity(name, new_quantity)
                elif menu_edit == 3:
                  new_price = input('Harga item baru\t: ')
                  try:
                    new_price = int(new_price)
                  except ValueError:
                    print(f'Harga item yang anda masukkan salah!!! nilai yang \
                    diterima adalah angka')
                  else:
                    trnsct_123.update_item_price(name, new_price)
                
                print('')
                print(trnsct_123)
                print('')
                          
            if menu_edit == 4:
              break
          
        elif menu == 3:
          delete_item = input('Item yang akan dihapus\t: ')
          trnsct_123.delete_item(delete_item)
          print(trnsct_123)

        elif menu == 4:
          trnsct_123.reset_transaction()
          print('Semua item berhasil didelete!')

        elif menu == 5:
          try:
            trnsct_123.check_order()
          except Exception:
            print('Terdapat kesalahan input data!!' )
          else:
            print('\nPemesanan sudah benar\n')
            trnsct_123.total_price()
        
        print('')
        print(tabulate(list_menu, headers = "firstrow"))
        menu = input('\nPilih menu\t: ')
        print('')

  if menu == 6:
    break