import random
import sys

def randomizer(Choiсe: int) -> int:
    if Choiсe < 0:
        raise ValueError("Пожалуйста, введите число корректно")
    result = random.randint(0, Choiсe)
    return result

try:
    __user__choice = int(input('До какого числа вы выбираете случайность: '))
    result = randomizer(__user__choice)
except ValueError:
    print("Пожалуста, введите число корректно ")
    sys.exit(1)

def Guess_number():
    try:
        while True:
            __user__quess = int(input('Угадайте число: '))
            if __user__quess == result:
                print('Поздравляю вы угадали число')
                return f'Загаданое число было: {__user__quess}'
            elif __user__quess < result:
                print(f'Загаданное число больше')
            else:
                print(f'Загаданное число меньше')
    except ValueError:
        print('Введите число корректно: ')




print(Guess_number())