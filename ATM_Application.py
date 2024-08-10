
# ATM - Bankamatik Uygulaması
# Çekilmek istenilen para bakiye tarafından karşılanabilir olmalı.
# Çekilmek istenen miktar hesap bakiyesinden fazla ise ek hesap kullanılması müşteriye sorulmalı.
# Müşteri evet derse ek hesap devreye girsin ve para çekilsin ardından kasa bilgileri güncellensin.Ek hesap çekmek istediği tutarı karşılamaz ise işlem iptal edilsin
# Hayır derse para çekme işlemi iptal edilsin.
# Müşterinin hesabına para girişi olduğunda ek hesap bakiyesi eksik ise ilk ek hesaba para girişi olsun ve kalan tutar  ana hesaba yatırılsın.
# Adamın balance ve additional balance'si çekilmek istenilen tutarı karşılamıyorsa feedback verilsin ve işlem iptal edilsin.
# Müşteri EFT İşlemi yapabilsin.

burak_account = {
    'account no': '12345',
    'full name': 'Burak Yılmaz',
    'pasword': '123',
    'balance': 3000,
    'additional balance': 1000

}

hakan_account = {
    'account no': '98765',
    'full name': 'Hakan Yılmaz',
    'pasword': '123',
    'balance': 5000,
    'additional balance': 1000

}

ipek_account = {
    'account no': '34567',
    'full name': 'İpek Yılmaz',
    'pasword': '123',
    'balance': 8000,
    'additional balance': 1000
}

users = [burak_account, hakan_account, ipek_account]



# region Menü
def menu(account: dict) -> None:
    print(f"""
    Welcome, {account['full name']}
    ===============================
    Withdrow Money  ==> 1
    Deposit Money   ==> 2
    Account Info    ==> 3
    EFT             ==> 4
    Exit            ==> 5
    """)
#endregion



# region Hesap Bilgisi
def show_account_info(account: dict) -> None:
    print(f'Account No : {account["account no"]}\n'
          f'Full Name : {account["full name"]}\n'
          f'Balance : {account["balance"]} n'
          f'Additional Balance : {account["additional balance"]}'
    )
#endregion



#region Bakiye Sonucu Bilgisi
def balance_result(account : dict) -> None:
    print(f'You have {account["balance"]} TL. in account No : {account["account no"]}\n'
          f'Additional Balance has {account["additional balance"]}')
#endregion



#region Para Çıkış İşlemi
def withdrow_money(account: dict, amount: int) -> None:
    if account['balance'] >= amount:
        account['balance'] -= amount

        print(' Do not forget to take maney')
        balance_result(account)
    else:
        total_balance = account['balance'] + account['additional balance']

        if total_balance >= amount:
            use_additional_balance = input(f'Ek Hesap Kullanılsın mı ("yes" or "no") : ').lower()

            match use_additional_balance:
                case 'yes':
                    amount_used_additional_balance = amount - account['balance']
                    account['balance'] = 0
                    account['additional balance'] -= amount_used_additional_balance
                    print(' Do not forget to take maney')
                    balance_result(account)

                case 'no':
                    print('Transaction has been cancaled')
                    balance_result(account)

                case _:
                    print('Plase choose valid answer. ("yes" or "no")')

        else:
            print(f'Insufficent total balance.Transaction has been cancaled')
#endregion



# region Para Giriş İşlemi
def deposit_money(account: dict, amount: int) -> None:
    account['balance'] += amount
    if account['additional balance'] <= 1000:
        transferred_amount = 1000 - account['additional balance']
        account['balance'] -= transferred_amount
        account['additional balance'] += transferred_amount


    balance_result(account)
# endregion



#region EFT İşlemi
def eft_transactions(sender_account: dict, receiver_account_no: str, amount: int) -> None:

    for user in users:
        if user['account no'] == receiver_account_no:
            withdrow_money(sender_account, amount)
            deposit_money(user, amount)
#endregion



# region Login
def login(account_no: str, password: str ) -> dict:
    account = {}
    for user in users:
        if user['account no'] == account_no and user['pasword'] == password:
            account = user
            break

    return account
#endregion



def main():
    user_account = login(
        account_no=input('Account no : '),
        password=input('password No : ')
    )
    if user_account != {}:
        menu(account=user_account)
        while True:
            process = input('Proces : ')
            match process:
                case '1':
                    withdrow_money(
                        account=user_account,
                        amount=int(input('Amount : '))
                    )
                case '2':
                    deposit_money(
                        account=user_account,
                        amount=int(input('Amount : '))
                    )
                case '3':
                    show_account_info(
                        account=user_account
                    )
                case '4':
                    eft_transactions(
                        sender_account=user_account,
                        receiver_account_no=input(f'Receiver Account : '),
                        amount=int(input('Amount : '))
                    )
                case '5':
                    print('Application has been closing..!')
                case _:
                    print('Please chooese a valid process..!')
    else:
        print(f'Authentiacation faild .Plase chesck your credentials .. ! ')

main()







