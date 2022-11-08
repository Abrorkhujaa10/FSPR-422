#    *
#   ***
#  *****
# *******
#    *
#    *


a = [2, 3, 4, 5, 6, 7]
chet = []
nechet = []
s = len(a)
for i in range(s):
    if a[i] % 2 == 0:
        chet.append(i+1)
    else:
        nechet.append(i+1)
print(chet)
print(nechet)


result = []
faranheits = [2, 3, 4, 5, 6]
for far in faranheits:
     celsius = (far - 32) * 5 / 9 
     if celsius >= 5:
         print("Слишком горячо")
         break
     elif celsius <= 10:
         print("Жить можно")
         result.append(celsius)
print(result)