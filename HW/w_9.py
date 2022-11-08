# a = [1, 2, 3, 4, 5, 6, 7]   Д/З
# for i in a:
#     i *=4
#     print(i)

# a = [1, 2, "hello", 3, 4, 5, 6, 7]
# for i in a:
#     a.pop(2)
#     i*=4 
#     print(i)

# s = [1, 2, "hello", 4, 5, 6, 7]
# b = []
# print(b)
# for val in a:
#     if isinstance(val, (int, float)):
#         b.append(val * 4)
# print(b)



a, b, *args = (2, 4, 4, 7, 8, 9, 0)
print(a, b, args)

for i in range(10):
    print(i)

print("Next range")
for i in range(4, 10): # 4 дан 9 гача
    print(i)

print("Next range")
for i in range(4, 10, 2):
    print(i)
    