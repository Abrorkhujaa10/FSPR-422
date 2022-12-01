class Marker:
    size = 17
    health = 10
    # переменные - атрибуты
    # функции - методы 
    # магическая  функция  или dunder функция
    def __init__(self, company, color, price):
        # переменные - атрибуты
        self.company = company
        self.color = color
        self.price = price


    # Метод класс
    def draw(self, line_length):
        if self.health <= 0:
            return f"Маркер истошен 0"
        self.health -= line_length

marker = Marker("Marker Inc.", "orange", 88)
marker_2 = Marker("Paket Inc", "Blue", 77)
marker_3 = Marker("Pocho Inc", "Yellow", 69)
# obj = {} # копия - экземпляр объекта словарь
# obj["age"] = 12

# print(dir(marker))
# print(dir(obj))
# print(type(a))
# print(marker.company)
# print(marker.color)
# print(marker.price)
# print(marker.size)

# print(marker_2.company)
# print(marker_2.color)
# print(marker_2.price)
# print(marker_2.size)

print("health =", marker.health)
marker.draw(5)
print("health =", marker.health)
marker.draw(5)
print("health =", marker.health)
print(marker.draw(5))
print("health =", marker.health)