import random

print("Привет! Это игра камень-ножницы-бумага. Сделай свой выбор и узнай, повезло тебе сегодня или нет :) Удачи!")
print("Твой выбор: ")
variants = ["камень", "ножницы", "бумага"]

def game():
    your_choice = input()
    pc_choice = random.choice(variants)
    if your_choice.lower() in variants:
        print("Окей, принято")
        print("Компьютер выбирает:", pc_choice)
        if your_choice == pc_choice:
            print("Ничья '_' ")
        elif (your_choice == "камень" and pc_choice == "ножницы") or (your_choice == "ножницы" and pc_choice == "бумага") or (your_choice == "бумага" and pc_choice == "камень"):
            print("Ты выиграл! :)")
        else:
            print("Ты проиграл! :(")
    else:
        print("Не понимаю твой ход")
game()

while True:
    print("Хочешь сыгарть еще?")
    answer = input()
    if answer.lower() == "нет":
        print("Окей, пока!")
        break
    elif answer.lower() == "да":
        print("Окей, давай еще раз!")
        game()
    else:
        print("Не понял твой ответ :(")