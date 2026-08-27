# class Student:
#     name = "karan"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)

# class Cars:
#     color = "red"
#     brand = "mustang"

# car1 = Cars()
# print(car1.color)
# print(car1.brand)

#parameterised constructor-:
# class Student:
#     college_name = "LNCTE"
    
#     def __init__(self, name, marks, age):
#         self.name = name
#         self.marks = marks
#         self.age = age
#     def welcome(self):
#         print("Welcome", self.name)

#     def get_marks(self):
#         return self.marks

# s1 = Student("arjun", 86, 18)
# s1.welcome()
# print(s1.get_marks())

# class Student :

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum = sum+val
#         print("Hello", self.name, "your avg score is", sum/3)


# s1 = Student("Jimmy", [93, 79, 82])
# s1.get_avg()

#Abstraction-:
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#         self.clutch = True
#         self.acc = True
#     print("Car started..")

# car1 = Car()