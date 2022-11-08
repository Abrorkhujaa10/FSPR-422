# Матрица 
[2,3,4,5,6,7] # вектор
matrix = [[2,3,4], [5,6,7]] # матрица 3 столбца и 2 строки
print(matrix[1][2]) 

# random = list(1) # error
# random = list(True) # error
random = list("Random  !)(!@#$") # error
splitted_string = "Split me ! random".split("me ! ") # ' '
print(random, splitted_string, ''.join(random),sep ="\n")

# Tuple - кортеж (итерабл/iterable)
numbers = (2,3,4,5,6)
print(numbers, numbers[3])
#           0      1     2       3 
numbers = ((4,5), 4.5, "fafa", [5,6,7])
print(numbers, numbers[3])

# numbers[1] = "Changed"
# Читать, создавать
 
numbers = (2, 4, 5, [4, 5])
numbers[3][0] = 24
print(numbers[3], numbers[3][0])

#              0       1   2  3   4   
numbers = [[2,3,4], [5,6], 5, 6, 7]
numbers[0][2] 