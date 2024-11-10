# Stok Crud İşlemlerini İçermektedir.

from uuid import uuid4
from pprint import pprint

products = {}
try:
    while True:
        proces = input('İşlem Türü Giriniz (exit, create, update, delete, list) : ')

        match proces:
            case 'exit':
                print('Uygulama Kapatılıyor.')
                break
            case 'create':
                name = input('Name : ')
                price = float(input('Stock : '))
                stock = int(input('Price : '))
                _id = str(uuid4())
                products[_id] = {'name': name, 'price': price, 'stock': stock}
                print(f'Stok Bilgisi Kaydedildi.')
            case 'update':
                product_id = input('Güncellenecek ID Bilgisi Gİriniz.')
                if product_id in products:                                              
                    name = input('Name : ')
                    price = float(input('Stock : '))
                    stock = int(input('Price : '))
                    products.update({product_id: {'name': name, 'price': price, 'stock': stock}})
                    print(f'{product_id} ID Güncellenmiştir.')
                else:
                    print(f'{product_id} Nolu ID Kayıtlarımızda Rastlanılmamıştır.')
            case 'delete':
                product_id = input('Silinecek ID Bilgisi Gİriniz.')
                if product_id in products:
                    del products[product_id]
                    print(f'{product_id} ID Kaydı Silinmiştir.')
                else:
                    print(f'{product_id} Nolu ID Kayıtlarımızda Rastlanılmamıştır.')
            case 'list':
                pprint(products)
            case _:
                print('Yanlış Giriş Tuşlaması')
except ValueError as err:
    print(f'Stock, Price Alanına Sayısal Değer Giriniz.')