# x = 6
# symbol = "*" 
# for i in range(x):
#     print(" " * (x-i-1) + "*" * (i*2+1))
# print(" " * (x-1)+symbol)
# print(" " * (x-1)+symbol)


# Функция 

if 1 == 1:
    print(True)

def greet():
    print('Hello')

# Вызоы Функций 
print('Вызов функций', greet())

def greet():
    return 'Hello' # return - вернуть

result = greet()
print(result)

# -------------------------------
def greet(name):
    print(f"Hello {name}")
greet("Behruz")
s = "Abror"
greet(s)
# greet( input("Input name:"))

def greet(name): # аргумент функция
    return f"Hello {name}"

print(greet("Azam"))
result = greet("Said")
print(result)


# Написать функцию, которая принимает список фарангейтов и возвращает список цельсия
faranheits = [30, 20, 19, 24, 45] # list
def fars_to_cels(faranheits):
    result = []
    for far in faranheits:
     celsius = (far - 32) * 5 / 9
     result.append(celsius)
    return result
print(fars_to_cels(faranheits))
    
