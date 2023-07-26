from decouple import config
from win_lose import check_win_lose

def play():
    slots = list(range(1, 31))
    money = float(config("MY_MONEY"))
    playing = True
    while playing:
        print(f"ваш счет {money}$")
        bet = float(input("сколько денег хотите поставить: "))
        user = int(input("на какой слот: "))
        chosen = user if user in slots else print('выберите от 1 до 30')
        win = check_win_lose(chosen)

        if win:
            money += 2 * bet
            print("вы выиграли.")
        else:
            money -= bet
            print("вы проиграли")

        choice = input("хотите еще сыграть? (д/н)")

        if choice.lower() != "н" or money == 0:
            playing = False
        if money > float(config("MY_MONEY")):
            print("вы выиграли!")
        elif money == float(config("MY_MONEY")):
            print("ничья")
        else:
            print("вы проиграли")
