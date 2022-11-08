# bool
# True | False 
# любое число что не ноль - это правда (True)
# если переменная пустая - то она ноль (False)
# True = 1 False = 0 

# print(False * 3)
x = 10 
# y = 20
# if x > y:
#     print(True)
# else:
#     print(False)

# "name surname".split() # ["name", "surname"]
# # a if condition else b 
# print( True if x > y else False)

# ==, !=, >, >=, <, <=, is, is not, in, not in, not, and, or

# {}, [], "", 0 - Не работает ложь

# if []:
#     print(True)

# if -19:
#     print(True)

name = "Behruz"
skill = "D2"
age = 20
surname = "Saidjonov"

# if name == "Sardor" and skill == "D2": # and - означает "и"
#     print(name,skill)
# else:
#     print("AND")

# if name == "Sardor" and skill == "D2": # or - означает "или"
#     print(name,skill)
# else:
#     print("OR")

# # not - нет =  отрицает
# if not age: # not = True -> False
#     print(age)
# else:
#     print("Age is False")

# #                   True            True
# #         True             True
# if (name == "Behruz" and age > 18) or skill == "D2":
#     print(name, age, skill)
# else:
#     print("Invalid name, age, skill")

# if name == "Behruz" and age > 22 or skill == "D2":
#     print(name, age, skill, "second output")
# else:
#     print("Invalid name, age, skill")

# is, == 
# is =  сравнивает id двух значений 
# == - не сравнивает значение 
# id()
a = 1
b = 1
print( id(a), id(b) )

t_1 = ()
t_2 = ()
# print( id(t_1), id(t_2) )
print( t_1 == t_2 )
print("tuple",t_1 is t_2 ) #False
# print("1 == 1", 1 == 1, 1 is 1)

# Изменяймые типы данных
# [] []
l_1 = [1, 2] # 1234567
l_2 = [1, 2] # 8987665
print(l_1 == l_2)
print(l_1 is l_2)

d_1 = {1: 1}
d_2 = {1: 1}
print("dict", d_1 == d_2 )
print("dict", d_1 is d_2 )

