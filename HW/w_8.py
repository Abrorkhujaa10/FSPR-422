s_strok = ' '
s_list = []
s_numebers = 0
a = [5, 3, 7, 9, "Abror", [3,4], "Agzamov", [4], 10.5]
for x in a:
    # print(x,type(x)) Проверает типы 
    if isinstance(x,str):
        s_strok = s_strok + x
    elif isinstance(x,list):
        s_list = s_list + x
    elif isinstance(x,int) or isinstance(x, float):
        s_numebers = s_numebers + x    
print(s_strok)
print(s_list)
print(s_numebers)

# a = int(input('xp'))
# if a <=100<=10<=50:
#     print("1 Уровень")
# else:
#     print()