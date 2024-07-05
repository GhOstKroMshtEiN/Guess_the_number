import random


def randomizer() -> int:
    while True:
        __user__choice = input('Enter the maximum number to choose a random number: ')
        if __user__choice.isdigit() and int(__user__choice) > 0:
            result = random.randint(0, int(__user__choice))
            return result
        else:
            print('Please enter a valid number')


result = randomizer()

def Guess_number():
    while True:
        __user__quess = input('Guess the number: ')
        if __user__quess.isdigit():
            __user__quess = int(__user__quess)
            if __user__quess == result:  # Alternatively, you could use int() here instead of adding line 21
                print('Congratulations, you guessed the number!')
                return f'The guessed number was: {__user__quess}'
            elif __user__quess < result:
                print('The guessed number is higher')
            else:
                print('The guessed number is lower')
        else:
            print('Please enter a valid number')


print(Guess_number())
