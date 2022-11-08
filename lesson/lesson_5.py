"""
Неизменяемый
    frozenset - множества
    tuple - кортеж
    int
    float
    str
    bool
    bin

Изменяемый 
    set - множества
    dict - словарь 
    list - список 

Прочитать 
    coplex
    decimal
    fraction

"""  

names = []
print(names)
names = list()
print(names)

#        0  1  2  3  4  5   6       7      8    10
names = [1, 2, 3, 4, 5, 6, 12.5, 'ABCD', True, None]
print(names)
names[0] = False
# names[7] = "name"
print(names[7][0]) # ABCD -> A 

#           0              1                2
names = [[2, 3, 4],[4.5, 5.6, 6.6],['go','go1', 'go2']]
print(names[2][2])

# Нарезка - slice 
# интерировать - проходиться по элементам интерируемых переменных (эти такие переменные,которые могуть хранить
# больше одного значения)

#          0  1  2   3   4   5   6
numbers = (4, 5, 6, 10, 22, 55, 500)
#         -7 -6 -5 -4   -3  -2  -1

# [начало:конец]
print( numbers[1:5] ) # 5 индекс
print( numbers[:],numbers)
print( numbers[1:])
print( numbers [:5])

# [начало:конец:шаг]
print("шаг", numbers[:6:2])
print("шаг", numbers[:6])
print("шаг", numbers[::2])
print("шаг", numbers[::10])
print("шаг", numbers[::-1])