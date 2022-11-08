# info = []
# for i in range(2): # Два раза пото - что range(2)
#     name = input("input name")
#     age = int(input("input age"))
#     info.append(
#         {
#             "age": age,
#             "name": name,

#         }
#     )
# print(info)

# result = []
# faranheits = [20, 140, 19, 24, 45]
# for far in faranheits:
#     celsius = (far - 32) * 5 / 9 
#     if celsius >= 50:
#         print("Слишком горячо")
#         break
#     elif celsius <= 5:
#         print("Жить можно")
#         result.append(celsius)
# print(result)

# **** 
# *  * 
# *  * 
# **** 

# star_width = star * square_line 
# print(star_width) 
# print(f"{star}  {star}") 
# print(f"{star}  {star}") 
# print(star_width)

square_line = 4
star = "*"
star_width = star * square_line  
for i in range(square_line):
    if i > 0 and i < (square_line - 1): # i < 0 and i < 5: 1 2 3 4 
        empty_space = " " * (square_line - 2) # 4 "    "
        print(f"{star}{empty_space}{star}")
    else:
        print(star * square_line)

i = 0
while i < 10: # True - while будет работать
    print("i=", 1) # 9
    i += 1 # 9 + 1 = 10

i = 0
while True:
    i += 1
    print("i=", i)
    if i == 100:
        break

names = [1, 2, 3, 4, 5, 6]
i = 0
while i < len(names): # 6
    print(names[i])
    i += 1


s = "ABCDEFG"
for i in range(len(s)):
    s[i]

for i, val in enumerate("ABCDEFG"):
    print(i, val)

s = [1, 1, 2, 3, 4, 4, 5, 3]
print(set(s))

d = [
    {
    3:"hello",
    2:"hello",
    1:"hello"
    }
]
s = d.sort()
print(d, sep="\n")