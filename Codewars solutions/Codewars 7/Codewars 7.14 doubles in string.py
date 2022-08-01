#An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
#Example: (Input --> Output)
#"Dermatoglyphics" --> true
#"aba" --> false
#"moOse" --> false (ignore letter case)

def is_isogram(s):
    s = s.lower()
    return len(set(s)) == len(s)
#АХУИТЕЛЬНОЕ РЕШЕНИЕ ЕСЛИ ДЛИННА ПОСЛЕ СОРТИРОВКИ РАВНА ДЛИННЕ ДО СОРТИРОВКИ ВОЗВРАЩАЕТ ТРУ ЕСЛИ НЕТ ТО ФОЛС
#Команда set УДАЛЯЕТ ВСЕ ПОВТОРЕНИЯ СИМВОЛОВ ИЛИ ЗНАЧЕНИЙ В ЛЮБОМ ТИПЕ ДАННЫХ!!