def ourder_of_args(name, default='go', *args, sep='seperator', username, end='\n', **kwargs):
    print(name, default, args, username, end, sep, kwargs)
ourder_of_args('Behruz', 123, 4, 5, 6, username='apo', end='not enter', sep='not sep', email='e@com', loot=[2, 3])


def func(*args, **kwargs):
    print(args, kwargs)
func(2, 3, 4, [5], user='Abror Agzamov', goal=("Chelsea Winner"))



def create_dict(keys):
    obj = {}
    for key in keys: # ['name', 'age', 'password']
        obj[key] = None
    print(obj)
create_dict(['name', 'age', 'password'])


matrix = []
a, b = 3,
for i in range(b):
    arr = []
    for j in range(a):
        arr.append(j)
    print(arr)
print(matrix)



