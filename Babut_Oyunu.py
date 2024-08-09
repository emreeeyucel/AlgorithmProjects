from pprint import pprint
from random import choice, randint


user_dict = {
    '1': {
        'user_name': 'beast',
        'password': '123',
        'safe': 1200
    },
    '2': {
        'user_name': 'savange',
        'password': '123',
        'safe': 2200
    }
}

bots = ['ahmet', 'fatma', 'mehmet', 'ayşe']
minimum_bet = 100




# Rakip Eşleşmesi ( bots listesinden random item döndüren fonkisyon )
def assing_default_bot(bot_list: list) -> str:
    return choice(bot_list)



# Bahis Kontrol
# KullanıcınIn oyun esnasında girdiği anlık bahis minimum bet'e eşit ve büyük kendi kasasından küçük ve eşit olmalıdır.
def is_bet_valid(current_bet: int, safe: int) -> bool:
    if minimum_bet <= current_bet <= safe:
        return True
    else:
        return False



# Çip Üretimi
# Login olan kullanıcıya günlük hediye 1000 ile 2000 arasında günlük çip hediye edelecektir. KALDIM
def gain_daily_chips() -> int:
    chip = randint(a=1000, b=2000)
    return chip



# Zar Atılması
def roll_dicle() -> int:
    return randint(a=2, b=12)



# Kullanıcının Sisteme Girişi (Login)
def login(user_name: str, password: str) -> dict:
    is_active = False
    user_id = ''
    for i in range(1, len(user_dict) + 1):
        if user_dict.get(str(i)).get('user_name') == user_name and user_dict.get(str(i)).get('password') == password:
            user_id = str(i)
            is_active = True
            break

    if is_active:
        return user_dict.get(user_id)
    else:
        return {}



# Yeni Üye Oluşturma (Sing up)
def sign_up(user_name: str, password: str,) -> None:
    user_names = []
    for i in range(1, len(user_dict) + 1):
        user_names.append(user_dict.get(str(i)).get('user_name'))
    if user_name not in user_names:
        user_dict[str(len(user_dict) + 1)] = {
            'user_name': user_name,
            'password': password,
            'safe': gain_daily_chips(),
        }
    print('accuount hass veen created')



# Çip Güncellemesi
# Her oyunun sonunda yada sisteme giriş yapıldığında kasayı güncelleyecektir.
def update_safe(user: dict, chip: int, status :bool) -> None:
    if status:
        user.update({
            'safe': user.get('safe') + chip})
        print(f' Congratualtaions {user.get("user_name")}\n'
              f'Your current safe is {user.get("safe")}')

    else:
        user.update({
            'safe': user.get('safe') - chip
        })

        print(f' You lost {user.get("user_name")}\n'
              f'Your current safe is  {user.get("safe")}')


def main():

    while True:
        first_process = input('Type a process : ("Sign In or Sign Up")  : ').lower()

        if first_process == 'sign up':
            sign_up(
                input('Username : '),
                input('Pasword : ')
            )

        elif first_process == 'sign in':
            login_user = login(
                input('Username : '),
                input('Pasword : ')
            )

            if login_user != {}:
                daily_chip = gain_daily_chips()
                update_safe(login_user, daily_chip, True)

                while True :
                    if login_user.get('safe') >= minimum_bet:
                        bet = int(input('please make a bet : '))

                        if is_bet_valid(bet, login_user.get('safe')):
                            rakip_player = assing_default_bot(bots)

                            print(f'Your oppent name is {rakip_player} \n'
                                  f'Lets play ')

                            player_1_roll = roll_dicle()
                            player_2_roll = roll_dicle()

                            print(f'Your dice are {player_1_roll}\n'
                                  f'{rakip_player} dice are  {player_2_roll}')

                            if player_1_roll > player_2_roll:
                                update_safe(login_user, (bet * 2), True)
                            elif player_2_roll > player_1_roll:
                                update_safe(login_user, bet, False)
                            else:
                                print('Player are tie ..!')

                        else:
                            print('Please make a valid  bet ')
                    else:
                        print(f'Your {login_user.get("safe")} safe is under the minimum table bet\n'
                              f'Do you want to buy any chips')
                        break
        else:
            print(f'Try again')

main()








