#Анонимные функции Лямда - Создает ф-цию не присваивая ей название лямда может быть там где синтаксис не позволяет использовать ДЕФ 
#Лямда Не может содержать в себе больше одной строки
#Возвращает площадь прямоугольника по длинам его сторон
from ast import Lambda


def rectangle_area(a, b):
    return a * b
print(rectangle_area(17, 14))
#LAMBDA
print((lambda a, b: a * b)(17, 14))

def maximum(a, b):
    if a > b:
        return a
    else:
        return b
print(maximum(25, 17))
#Аналог проще
print((lambda a, b: a if a > b else b)(25, 17))