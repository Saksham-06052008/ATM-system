#delete-:
# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("saksham")
# print(s1.name)
# del s1.name
# print(s1.name)

#Private attribution & Methods-:
# class Person:
#     __name = "anonymous"

#     def __hello(self):
#         print("hello person!")
#     def welcome(self):
#         self.__hello()
# p1 = Person()
# print(p1.welcome())

#single Inheritance-:
#multi-level Inheritance-:
# class Car:
#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stoped")

# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("diesel")
# car1.start()

#multipal Inheritance-:

# class A:
#     varA = "Welcome to class A"

# class B:
#     varB = "Welcome to class B"

# class C(A, B):
#     varC = "Welcome to class C"

# c1 = C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

# class Car:
#     def __init__(self, type):
#             self.type = type
#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stoped")

# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type)
#         super().start()

# car1 = ToyotaCar("prius", "EV")
# print(car1.type)

#Class Method-:

# class Person:
#     name = "anonymous"

#     #def changename(self, name):
#         #Person.name = name
#     @classmethod
#     def changename(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changename("Saksham sharma")
# print(p1.name)
# print(Person.name)

#without using Property-:
# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.percentage = str((self.phy+self.chem+self.math)/3) + "%"


#     def calcPercentage(self):
#         self.percentage = str((self.phy+self.chem+self.math)/3) + "%"

# stud1 = Student(79, 65, 94)
# print(stud1.percentage)
# stud1.phy = 94
# stud1.calcPercentage()
# print(stud1.percentage)

#with using Property-:
# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math

#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.math)/3) + "%"

# stud1 = Student(79, 65, 94)
# print(stud1.percentage)
# stud1.phy = 94
# print(stud1.percentage)

#Polymorphism-operator overloding:
# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i +", self.img,"j")

#     def __add__(self, num2):
#         newreal = self.real + num2.real
#         newimg = self.img + num2.img
#         return Complex(newreal, newimg)
#     def __sub__(self, num2):
#             newreal = self.real - num2.real
#             newimg = self.img - num2.img
#             return Complex(newreal, newimg)
        
# num1 = Complex(1, 3)
# num1.showNumber()
# num2 = Complex(4, 7)
# num2.showNumber()

# # num3 = num1.add(num2) #without method
# # num3.showNumber()
# num3 = num1 - num2
# num3.showNumber()
