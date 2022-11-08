# LEGB - Local Enclosed Global Built-in
# ЛВГВ - Локальный Вложенный Глобальный Встроенный 

print(print) # Встроенный 

# любой объект 
name = 'Behruz'

def get_name():
    name = 'George' # Локальный
    print(name)

# get_name()

name = 'Dave'

def spam():
    global name # импортируем глабальную переменную
    name = 'Guido'

spam()
print(name)


def foo(items):
    items.append(42)

a = [1, 2, 3]
foo(a)
print(a)

# vs

def bar(items):
    items = [4, 5, 6]

b = [1, 2, 3]
bar(b)
print('b не поменялось', b)

def parent():
    a = 5
    return a
print('не выложенный', parent()) # 5 

# local enclosed Global Builtin
def parent():
    # enclosed
    a = 5
    def answer():
        # local
        return a
    return answer()
print("выложенный", parent()) # 5

a = 20
def parent():
    # enclosed
    a = 5
    def answer():
        # local
        a = 10
        def get():
            return a
        return get()
    return answer()

print('Вложенный', parent())


def outer():
    # enclosed
    x = 'Local'
    def inner():
        #local
        nonlocal x
        x = 'Non Local'
        print('inner', x)
    inner()
    print('outer', x)
outer()

name = "Dave"

def spam():
    global name
    name = "Abror"
spam()
print(name)

