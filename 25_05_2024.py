def score():
    item = ["Время","Книги","Семья"]
    print("Угадать загаданное слов")
    for i in range(0,3):
        yourword=input("Ваше слово")
        if yourword in item:
            print("Вы угадали")
            break
        else:
            print("Вы не угадали")
score()

def score():
    Hero = {}
    for i in range(1,4):
        Namehero=input(f"Имя героя {i}")
        itemhero=input("Его вещи")
        Hero[Namehero]=itemhero
    print(Hero)
score()

message = [("We ",), "rec", {"r": "o"}, {"o": "r"}, {"m1": "ded "},
           {"m3": ["a "], "m4": {"m5": "UFO"}}]
def decode_message(message):
    decoded_message = ""
    stack = [message]

    while stack:
        current = stack.pop()
        if isinstance(current, tuple):
            decoded_message += current[0]
        elif isinstance(current, dict):
            for key, value in current.items():
                if isinstance(value, dict) or isinstance(value, list):
                    stack.append(value)
                else:
                    decoded_message += value
        elif isinstance(current, list):
            for item in reversed(current):
                stack.append(item)

    return decoded_message



secret_message = decode_message(message)
print(secret_message)