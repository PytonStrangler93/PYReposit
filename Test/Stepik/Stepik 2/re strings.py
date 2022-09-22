# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
# Примечание:
# Считать все строки по одной из стандартного потока ввода вы можете, например, так
# import sys
# for line in sys.stdin:
#     line = line.rstrip()
#     # process line
# Sample Input:
# catcat
# cat and cat
# catac
# cat
# ccaatt
# Sample Output:
# catcat
# cat and cat

import re
import sys

for line in sys.stdin:
	line = line.rstrip()
	a = r".*?cat.*?cat.*?"
	x = re.search(a, line)
	if x:
		print(line)

# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве слова.
# Примечание:
# Для работы со словами используйте группы символов \b и \B.
# Описание этих групп вы можете найти в документации.
# Sample Input:
# cat
# catapult and cat
# catcat
# concat
# Cat
# "cat"
# !cat?
# Sample Output:
# cat
# catapult and cat
# "cat"
# !cat?


for line in sys.stdin:
	line = line.rstrip()
	x = re.search(r"\bcat\b", line)
	if x:
		print(line)




for line in sys.stdin:
	line = line.rstrip()
	x = re.findall(r"\\", line)
	# ИЩЕТ СИМВОЛ \ если вы хотите задать соответствие символу '*', в шаблоне вам необходимо
	# указать '\*'. Это предотвратит трактование '*' как метасимвола с особым значением.
	if x:
		print(line)

	# Вам дана последовательность строк.
	# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
	# Sample Input:
	# blabla is a tandem repetition
	# 123123 is good too
	# go go
	# aaa
	# Sample Output:
	# blabla is a tandem repetition
	# 123123 is good too

for line in sys.stdin:
	line = line.rstrip()
	x = r"\b(.+)\1\b"
	# . любой символ .+ 1 или более любых символов \1 повтор группы символов
	# (.+)\1 любой символ 1 или более раз должен повторяться в слове
	if re.search(x, line):
		print(line)

# Вам дана последовательность строк.
# В каждой строке замените все вхождения подстроки "human" на подстроку
# "computer" и выведите полученные строки.
# Sample Input:
# I need to understand the human mind
# humanity
# Sample Output:
# I need to understand the computer mind
# computer
for line in sys.stdin:
	line = line.rstrip()
	print(re.sub(r"human", 'computer', line))

# Вам дана последовательность строк.
# В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a"
# (регистр не важен), на слово "argh".
# Примечание:
# Обратите внимание на параметр count у функции sub.
# Sample Input:
# There’ll be no more "Aaaaaaaaaaaaaaa"
# AaAaAaA AaAaAaA
# Sample Output:
# There’ll be no more "argh"
# argh AaAaAaA

for line in sys.stdin:
	line = line.rstrip()
	print(re.sub(r'[Aa]+\b|\b[Aa]+', 'argh', line, count=1, flags=0))



# Вам дана последовательность строк.
# В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
# Буквой считается символ из группы \w.

pattern = r'(\w)\1+'

for line in sys.stdin:
	print(re.sub(pattern, r'\1', line.rstrip()))

