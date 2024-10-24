# Çalışmamızda bir uygulamada alınan hataların "LOG KAYITLARINI" kayıt edeceğiz.
# Ayrıca şifreleyerek log tutacağız.

from socket import gethostname, gethostbyname
from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

machine_name = gethostname()
ip_address = gethostbyname(gethostname())
error_date = datetime.now()


try:
    with open(
        file='log.txt',
        mode='w',
        encoding='utf-8'
    ) as file:
        file.write('Appcalication Exception Logns\n')
    try:
        age = int(input('Please Type Age : '))
        print(f'Your Age Is {age}')
    except ValueError as err:
        key = get_random_bytes(16)
        obj = AES.new(key, AES.MODE_EAX)
        chipper_text = obj.encrypt(b'valueerorhappen')

        with open(
            file='log.txt',
            mode='a',
            encoding='utf-8'
        ) as file:
            file.write(str(chipper_text))
            file.write(' ||  ')
            file.write(f'Machine Name : {machine_name}')
            file.write(' ||  ')
            file.write(f'Ip Adress : {ip_address}')
            file.write(' ||  ')
            file.write(f'Eror Date  : {error_date}')
            file.write(' ||  ')
        print('Age Information Have Not Any Character')
except IOError as err:
    print(f'{err.__doc__}')





# Kodun Yapısı ve Mantığı;

#  İlk try bloğu:
# log.txt dosyasını yazma modunda açar ve başlangıç mesajını yazar.
# Dosya açma veya yazma sırasında bir IOError oluşursa, bu hata yakalanır ve ilgili mesaj ekrana yazdırılır.

# İkinci try bloğu:
# Kullanıcıdan yaş bilgisini alır ve tam sayı olarak dönüştürür.
# Eğer kullanıcı geçerli bir sayı girmezse ValueError oluşur ve bu hata yakalanır.
# ValueError oluştuğunda, AES şifreleme işlemi yapılır ve şifrelenmiş hata mesajı ile ek bilgileri log dosyasına yazar.