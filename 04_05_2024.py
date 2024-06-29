#1
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


num1 = 36
num2 = 48
result = gcd(num1, num2)
print(f"Наибольший общий делитель чисел {num1} и {num2} равен {result}")



#2
import random


def generate_number():
    return random.sample(range(0, 10), 4)


def check_guess(secret, guess):
    bulls = 0
    cows = 0

    for i in range(4):
        if guess[i] == secret[i]:
            cows += 1
        elif guess[i] in secret:
            bulls += 1

    return bulls, cows


def play_game(secret, attempts=1):
    guess = input("Введите ваше четырёхзначное число: ")

    if len(guess) != 4 or not guess.isdigit():
        print("Пожалуйста, введите четырёхзначное число.")
        return play_game(secret, attempts)

    guess = [int(digit) for digit in guess]
    bulls, cows = check_guess(secret, guess)

    print(f"Быки: {bulls}, Коровы: {cows}")

    if cows == 4:
        print(f"Вы угадали число! Количество попыток: {attempts}")
    else:
        return play_game(secret, attempts + 1)


if __name__ == 'main':
    secret_number = generate_number()
    print("Добро пожаловать в игру 'Быки и коровы'!")
    play_game(secret_number)