import math
import random

print('Добро пожаловать в числовую угадайку')
number = random.randint(1,100)
print(number)
count_of_guesses = math.ceil(math.log2(number))
print(count_of_guesses)
counter_of_guesses = 0


def is_valid(text):
    return True if type(text) == int and 1 <= text <= 100 else False


while True:
    print('Введите целое число от 1 до 100') # GUESSING
    x = int(input())
    if is_valid(x):
        if x < number:
            print("Ваше число меньше загаданного, попробуйте еще разок!")
            counter_of_guesses += 1
            continue
        elif x > number:
            print("Ваше число больше загаданного, попробуйте еще разок")
            counter_of_guesses += 1
            continue
        else:
            print('Угадал говнила, поздравляем!')
            print('Пиздуй кодить дальше')
            break
    else:
        print('От хуйло, написано же, целое число от одного до 100!!!!')

if counter_of_guesses <= count_of_guesses:
    print('АХУЭННО!!')
else:
    print('ЧТО ТО В ПИЗДУ ВСЕ!')
    


