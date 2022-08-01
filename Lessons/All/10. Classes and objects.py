# Питон это обьектно ориентированный язык программирования - парадигма основанная на представлении прогр в виде совокупн обьектов являющихся
from pyclbr import Class


class House(): #Супер КЛАСС (Родитель)
    '''House revue'''
    def __init__(self, street, number): #Экземпляр класса
        '''House optioms'''
        self.street = street
        self.number = number
        self.age = 0 #Параметр по умолчанию не ссылается на описание метода
    def build(self): #Экземпляр класса
        '''Build a house'''
        print('House on street ' + self.street + 'on number ' + str(self.number) + ' already build.')
    def age_house(self, year):
        '''Age of house'''
        self.age += year
        
House1 = House('Kharkiv ', 20)
House2 = House('Kharkiv ', 21)

print(House1.street) #Если мы обращаемся к свойству то через принт

House2.build() #Если мы обращаемся к методу то через точку с пустыми скобками

House1.age_house(5) #Добавляем возраст дому

print(House1.age)
#НАСЛЕДОВАНИЕ!! Можно создать класс но не с нуля а наследуемый из предидущего.Он будет называться классом потомком
#Наследует все но может иметь свои особенности. или переопределять существующие.
class ProspectHouse(House): #Суб класс (Дочерний)
    '''Son of house'''
    def __init__(self, prospect, number):
        super().__init__(self, number)
        self.prospect = prospect
        
PrHouse = ProspectHouse('Lenin ', 5)

print(PrHouse.prospect)