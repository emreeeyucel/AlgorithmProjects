
from uuid import uuid4
from pprint import pprint

products = {}


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
            if product_id in products:                                              # Çoklu ID olduğundan kaynaklı içinde arama yapılacaktır.
                name = input('Name : ')
                price = float(input('Stock : '))
                stock = int(input('Price : '))
                products.update({product_id: {'name': name, 'price': price, 'stock': stock}})
                print(f'{product_id} ID Güncellenmiştir.')
            else:
                print(f'{product_id} Nolu ID Kayıtlarımızda Rastlanılmamıştır.')

        case 'delete':
            pass
        case 'list':
            pprint(products)
        case _:
            print('Yanlış Giriş Tuşlaması')