#Файлы с кодом на языке питон которые содержат в себе фрагменты кода
import math
print(math.factorial(10))
#Можно изменить название модуля по типу import math as n и в дальнейшем вместо math писать n
import math as n
print(n.factorial(10))
#можно из модуля импортировать только кусочек
from math import factorial #Можно факториал as "измененное имя если долго прописывать"
print(factorial(10))
#Вызов постороннего модуля, модуль должен находиться в той-же папке что и исполняющий файл и должен называться простым именем латиницей
import MYMODULE
MYMODULE.privet()