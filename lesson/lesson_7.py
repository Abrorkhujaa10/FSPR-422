# # Интерируемый - iterable (Исчичляемый) Это те переменные которые хранят больше одного значения
# names = [1, 3, 4, 5] #3
# print( type(names), names[3])
# names = ()
# print( type(names) )

# # Dictionary - Словарь
# # Ключом словаря могут быть только не изменяемые типы переменных

# user_data = {
#     "Ключь": "Значение",
#    1: None,
#    2: 21,
#    3: 6.7,
#    4: [2,3,4],
#    5: [5,6,7],
#    6: {"key": "Другой словарь"}
#    # [1]:23, # error
#    # (2, 3, [2, 3]): "Error", # Кортеж можно использовать как ключь, но не рекомендуеться
#    }
#    # 40 - 50 sadfghgasdfg
# print(type(user_data), user_data, user_data["Ключь"], sep="\n" )

# a = {
#     "Texnomart":"Asia"
# }
# print(a["Texnomart"])

# user_data = {
#     "username": "Gobby",
#     "password": "2rtr123r",
#     "age": 18, # has qwerjk
#     "age": 22, # qwerjk
# }
# print( user_data ["age"])

# user_data = { 
#     "username": "Gobby",
#     "password": "2rtr123r",
#     "age": 18, # has qwerjk
#     "age": 22, # qwerjk
# }

# # user_data = [
# #     {
# #         "username": "Gobby",
# #         "password": "2rtr123r",
# #         "age": 18,
# #     },
# #     {
# #         "username": "Apo",
# #         "password": "2rfdtr123r",
# #         "age": 14,
# #     },
# # ]
# # print ( user_data [0]["username"],user_data[0]["age"] )

# user_data["username"] = "Alabasta"
# print(user_data.keys(), user_data.values(), user_data.items(), sep = "\n")

# # dict_keys(['username', 'password', 'age'])
# # dict_values(['Alabasta', '2rtr123r', 22])
# # dict_items([('username', 'Alabasta'), ('password', '2rtr123r'), ('age', 22)])

# user_list = list(user_data.values()) #
# print(user_list)

# # print( user_data["unexisting"] ) # error
# print("get", user_data.get("age"), user_data.get("unexisting"))




# set - Множества
# нельзя индексировать
# можно менять через методы  или циклы 

numbers = {2, 3, 4, "hello", 2, 4}
print(numbers)
numbers = {} # dict
print( type(numbers) )
numbers = set()
print( type(numbers) )

remove_duplicates = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, "AA", "BB", "AA"]
result = list(set(remove_duplicates))
print(remove_duplicates, list(set(remove_duplicates)), result, sep = "\n")
