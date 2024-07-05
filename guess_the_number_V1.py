import random


def randomizer(Choiсe: int) -> int:
    result = random.randint(0, Choiсe)
    return result


__user__choice = int(input('До какого числа вы выбираете случайность: '))
result = randomizer(__user__choice)


def Guess_number():
        while True:
            __user__quess = int(input('Угадайте число: '))
            if __user__quess == result:
                print('Поздравляю вы угадали число')
                return f'Загаданое число было: {__user__quess}'
            elif __user__quess < result:
                print(f'Загаданное число больше')
            else:
                print(f'Загаданное число меньше')


print(Guess_number())
