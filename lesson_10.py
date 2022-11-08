for val in [1, 2, 3, 4, 5, [6, 7, 8, 5, 6], (4, 5, 6)]:
    if isinstance(val, (list, set, tuple)):
        for i in val:
            print(i)
    else:
        print(val)

a, b, *args = (2, 4, 4, 7, 8, 9, 0)
print(a, b, args)

for i in range(10):
    print(i)

print("Next range")
for i in range(4, 10): # 4 дан 9 гача
    print(i)

print("Next range")
for i in range(4, 10, 2): # 4 дан 9 гача 2 хар икки кадам ташаб
    print(i)

# continue / break / pass
numbers = [1, 2, 3, 4, 5, 6, 7]
for val in numbers:
    if val == 5 or val == 7:
        print(f"пропустить {val}")
        continue # -> for
    print("val=", val)
    

numbers = [1, 2, 3, 4, 5, 6, 7]
for val in numbers:
    if val == 5 or val == 7:
        print(f"выйти из цикла {val}")
        continue # -> for
    print("val=", val)

if 1 == 1:
    pass
