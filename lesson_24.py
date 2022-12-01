class Student: 
    def __init__(self, first_name, last_name, grades=[]): 
        self.first_name = first_name 
        self.last_name = last_name 
        self.grades = list(grades) # [] 
     
    def add_grade(self, grade): 
        self.grades.append(grade) 
     
    def get_average(self): 
        return sum(self.grades) / len(self.grades) 
 
johnDoe = Student('John', 'Doe') 
janeDoe = Student('Jane', 'Doe') 
jamesSmith = Student('James', 'Smith') 
jennaSmith = Student('Jenna', 'Smith') 
students = johnDoe, janeDoe, jamesSmith, jennaSmith 
 
firstAssessmentGrades = [63, 92, 82, 75] 
for i, student in enumerate(students): 
    student.add_grade(firstAssessmentGrades[i]) 
 
for i, student in enumerate(students): 
    print(student.grades[0], firstAssessmentGrades[i])

class GrandFahter:
    house = True

    def __init__(self, name, job, hobby, bank_accaunt):
        self.name = name
        self.job = job
        self.hobby = hobby
        self.bank_accaunt = bank_accaunt

    def spend(self, amount):
        self.bank_accaunt -= amount

    def income(self, amount):
        self.bank_accaunt += amount

class Mother:
    cooked_foot = ""
    def cook(self, products):
        if "carrot" in products and "meat" in products and "rice" in products:
            self.cooked_foot = "plov"
        else:
            print("No")
        


class Child(GrandFahter, Mother):
    def __init__(self, name, job, hobby, bank_accaunt, age):
        self.age = age
        super().__init__(name, job, hobby, bank_accaunt)
 
    def cook(self, products):
        super().cook(products)
        if "масло" in products and "баклажан" in products and "помидор" in products:
            self.cooked_foot = "Жаренный Баклажан"


child = Child("Behruz", "IT", "hiking", 100000, 21)
print(child.name, child.hobby, child.age)
child.spend(700)
print(child.bank_accaunt)
child.income(500)
print(child.bank_accaunt)

child.cook(["масло", "баклажан", "помидор"])
print(child.cooked_foot)
child.cook(["rice","carrot" ])
print(child.cooked_foot)