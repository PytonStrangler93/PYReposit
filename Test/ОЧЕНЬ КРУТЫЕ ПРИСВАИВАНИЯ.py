###ОЧЕНЬ КРУТЫЕ ПРИСВАИВАНИЯ
    
[print('YES' if 'воскресенье' in i or 'суббота' in i else 'NO') for i in [input()]]
print('YES' if 'суббота' in (i := input()) or 'воскресенье' in i else 'NO')
print((lambda x: ['NO', 'YES']['суббота' in x or 'воскресенье' in x ])(input()))
x = input()
print(('NO', 'YES')[('суббота' in x or 'воскресенье' in x)])
[print('Python is awesome!') for _ in 'десять раз']

for i in "Qzuipo!bxftpnf\" "*10:
    print(chr(ord(i)-1), end="")
# 1) 
# ord (аргумент)
# аргумент – в качестве аргумента принимается строка с символом Юникода. 
# Обязательный аргумент. 
# Функция ord( ) возвращает целое число порядковый номер символа Юникода переданного в 
# качестве аргумента.
# В данном случае получаем некоторую цифру от буквы Q, из этой цифры вычитаем один, 
# то есть движемся как бы по алфавиту Юникода влево. То есть буква Q станет буквой Р, 
# это первая буква нашей фразы «Python...!»
# 2)
# chr(аргумент)
# аргумент – любое целое число в диапазоне от 0 до 1 114 111 или 
# если в шестнадцатеричной системе от 0 до 10FFFF(0x10FFFF). Обязательный аргумент. 
# Функция chr( ) возвращает строку (str) с символом Юникода номер 
# которого равен значению аргумента.

[[print(i, n) for i in range(10)] for n in [input()]]
n = input(); [print(i, n) for i in range(10)]
[[print(f"Квадрат числа {i} равен {i**2}") for i in range(a+1)] for a in [int(input())]]

# на входе два слова имя и фамилия тут проверка на капиталайз каждого слова
# типо если оба слова начинаются с большой буквы то да
s = input()
print(('NO', 'YES')[s == s.title()])

#обрати внимание на эндвиз первым аргументом принимает два значения
print("YES" if input().endswith(('.com','.ru')) else 'NO')

# кутой лист компрехеншон с преобразованием из числа в знак ASCII
print(*[chr(i) for i in range(int(input()),int(input())+1)], end=' ' )
    
#На вход программе подается строка текста. Напишите программу, которая выводит индекс второго вхождения буквы «f». 
# Если буква «f» встречается только один раз, выведите число -1, а если не встречается ни разу, выведите число -2.
# Формат входных данных 
# На вход программе подается строка текста.
print(-2 + 1*min(2, len(indexes := [i for i, x in enumerate(input()) if x == 'f'])) or indexes[1])

print((lambda x: [i for i in range(1, x + 1) if x % i == 0])(int(input())))


def is_password_good(password):
    upp = [i for i in password if i.isupper()]
    low = [i for i in password if i.islower()]
    dig = [i for i in password if i.isdigit()]
    return all([len(password) >= 8, upp, low, dig])


txt = input()
print(is_password_good(txt))