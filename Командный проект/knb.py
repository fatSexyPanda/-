import random

def get_computer_choice():
    choices = ["камень", "ножницы", "бумага"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "ничья"
    elif (player_choice == "камень" and computer_choice == "ножницы") or \
         (player_choice == "ножницы" and computer_choice == "бумага") or \
         (player_choice == "бумага" and computer_choice == "камень"):
        return "Вы победили"
    else:
        return "Компьютер победил"

def main():
    print("Добро пожаловать в игру 'Камень, ножницы, бумага'")
    print("Для выхода введите 'выход'.")

    while True:
        player_choice = input("Ваш выбор (камень, ножницы, бумага): ").lower()
        if player_choice == "выход":
            print("Спасибо за игру")
            break
        elif player_choice not in ["камень", "ножницы", "бумага"]:
            print("Некорректный ввод. Попробуйте еще раз.")
            continue

        computer_choice = get_computer_choice()
        print(f"Компьютер выбрал: {computer_choice}")

        winner = determine_winner(player_choice, computer_choice)
        print(winner)

if __name__ == "__main__":
    main()
