class PlayerCharacter:
    membership = True # Доступ для всех образов класса)
    def __init__(self, hobby, name = "Abror", age = 0):
        self.name = name
        self.age = age
        self.hobby = hobby

    def _welcome(self):
        return "HEEEEEEEEEY"

    def shouts(self):
        return f"{self._welcome()} My name is {self.name} and my hobby is {self.hobby}"

    @classmethod
    def adding_things_2(cls, num1, num2):
        return cls(num1 + num2)

    @staticmethod
    def multiply(a, b):
        return a * b 
    
player_1 = PlayerCharacter("sleeping", "Azam", 21)
# print(player_1.multiply(77, 5))
print(player_1.shouts())

# print(player_1.name, player_1.age)

# player_3 = PlayerCharacter.adding_things_2(33, 77)
# print(player_3.age, player_3.name)