
# i = 1  #3rd using while
# while i <= 50:
#     if(i%2 == 0):
#         print(i)
#     i = i+1
# for i in range(2, 51, 2): #3rd using for and range
#     print(i)

# i = 1  #4th using while
# while i <= 50:
#     if(i%2 != 0):
#         print(i)
#     i = i+1

# num = int(input("enter a number: "))  #5th using while
# i = 1
# while i <= 10:
#     print(num,"*",i,"=",num*i)
#     i = i+1
# num = int(input("Enter a Number: "))  #5th using for
# for i in range(1, 11):
#     print(num,"*",i,"=",num*i)

# val = int(input("Enter a number : "))  #6th using while
# sum = 0
# i = 1
# while i<=val:
#     sum = sum+i
#     i = i+1
# print(sum)
# num = int(input("Enter a Number : "))  #6th using for
# sum = 0
# i = 1
# for i in range(1, num+1):
#     sum = sum+i
# print(sum)

# num = int(input("Enter a number: "))  #7th using a while
# factorial = 1
# i = 1
# while i<=num:
#     factorial = factorial*i
#     i = i+1
# print(factorial)
# val = int(input("enter a number: "))  #7th using for
# factorial = 1
# i = 1
# for i in range(1, val+1):
#     factorial = factorial*i
# print(factorial)

#Lecture 6th on Functions and Recurtion-:
# def calc_sum(a, b):
#     sum = a+b
#     return sum
# def calc_minus(a, b):
#     minus = a-b
#     return minus
# def calc_prod(a, b):
#     prod = a*b
#     return prod
# def calc_div(a, b):
#     if(b == 0):
#         print(a,"/",b,"= Undefined")
#     else:
#         print(a,"/",b,"=",a/b)
# def calc_mod(a, b):
#     if(b==0):
#         print(a,"%",b,"= Undefined")
#     else:
#         print(a,"%",b,"=", a%b)

# num1 = int(input("Enter 1st number : "))
# opr = input("Enter operator : ")
# num2 = int(input("Enter 2nd number : "))

# if(opr == "+"):
#     print(num1,"+",num2,"=", calc_sum(num1, num2))
# elif(opr == "-"):
#     print(num1,"-",num2,"=", calc_minus(num1, num2))
# elif(opr == "*"):
#     print(num1,"*",num2,"=", calc_prod(num1, num2))
# elif(opr == "/"):
#     calc_div(num1, num2)
# elif(opr == "%"):
#     calc_mod(num1, num2)
# else:
#     print("Invalid operation")


#questions on file
# with open("practice.txt", "r")as f:
#     data = f.read()

# new_data = data.replace("python", "java")
# print(new_data)
# with open("practice.txt", "w")as f:
#     f.write(new_data)

# with open("practice.txt", "r")as f:
#     data = f.read()
#     words = data.split()
#     print(len(words))

# with open("practice.txt", "r")as f:
#     data = f.read()
#     lines = data.count("\n")
#     print(lines+1)
# word = input("Enter a word : ")
# def check_word(word):
#     with open("practice.txt", "r")as f:
#         data = f.read()
#         if(word in data):
#             print("FOUND")
#         else:
#             print("NOT found")

# check_word(word)

#final lecture-:
#que1

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

# s1 = Student("Saksham", 86)
# print(s1.name , s1.marks)

#que2
# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def get_area(self):
#         return self.length*self.breadth

# r1 = Rectangle(12, 4)
# r2 = Rectangle(26, 16)
# print(r2.get_area())

#que3
# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance = self.balance+amount
#         print("Rs.", amount, "was deposited")
#         print("Total balance is Rs.",self.balance)
#     def withdraw(self, amount):
#         self.balance = self.balance-amount
#         print("Rs.", amount ,"withdrawn")
#         print("Remaining balance is Rs.",self.balance)

# a1 = BankAccount("Saksham", 50000)
# a1.withdraw(25000)
# print(a1.balance)

#que4
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def result(self):
#         if(self.marks >= 37):
#             print("Pass")
#         else:
#             print("Fail!")

# s1 = Student("Saksham", 45)
# s1.result()

#que5
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def annual_salary(self):
#         return self.salary*12

# e1 = Employee("Saksham", 60000)
# print(e1.annual_salary())

#que6
# class Car:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#     def show_details(self):
#         print("Brand :", self.brand)
#         print("Model :", self.model)
#         print("Price :", self.price)
# c1 = Car("Toyota", "Fortuner", 5500000)
# c1.show_details()

#que7
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# class Student(Person):
#     def __init__(self, name, age, marks):
#         super().__init__(name, age)
#         self.marks = marks

# s1 = Student("Rakhi", 17, 89)
# print(s1.name, s1.age, s1.marks)

#Revision problems - lecture_one
# a = float(input("Enter length : "))
# b = float(input("Enter width : "))
# print("Area = ",a*b)

# user = int(input("Enter your present age : "))
# new_age = user+10
# print("In 10 years you'll be",new_age ,"years old")

# a = int(input("enter first no. : "))
# b = int(input("enter second no. : "))
# if(a >= b):
#     print("true")
# else:
#     print("false")

#Lectur_two -:

# str = "Apple"
# print(str[-3 : -1])

# text = "i am a coder"
# print(text.capitalize())
# print(text.count("a"))

# str = input("Enter a string : ")
# print(len(str))
# if(len(str)%2 == 0):
#     print("Even length")
# else:
#     print("Odd length")
#
# user_str = input("Enter a string : ")
# find = user_str.find("$")
# if(find!=-1):
#     print("Found at", find)
# elif(find==-1):
#     print("Not Found")

# marks = int(input("Enter marks : "))
# if(marks >= 90):
#     print("Excellent you got 'A+' grade")
# elif(90 > marks >= 80):
#     print("Good you got 'A' grade")
# elif(80 > marks >= 70):
#     print("keep it up you got 'B' grade")
# elif(70 > marks >= 60):
#     print("Need improvement 'C' grade")
# elif(60 > marks >= 50):
#     print("Very poor just got 'D' grade")
# elif(50 > marks):
#     print("Failed, got 'E' grade")
# else:
#     print("Error")

#Lecture 3rd -:

# numbers = [10, 20, 30, 40, 50]
# numbers[2] = 35
# print(numbers[1 : 4])

# scores = [45, 12, 89, 33, 67]
# scores.sort(reverse=True)
# scores.insert(0 ,100)
# print(scores)

# my_tupple = (5, 10, 15, 18)
# tempo_list = list(my_tupple)
# tempo_list[1] = 20
# my_tupple = tuple(tempo_list)
# print(my_tupple)

# data = (10, 20, 30, 20, 40, 20)
# print(data.count(20))
# print(data.index(20))

# lst = list(input("Enter a list : "))
# lst_new = lst.copy()
# lst_new.reverse()
# if(lst_new == lst):
#     print("This is a palindrome")
# else:
#     print("Not a palindrome")

# vals = [10, 20, 30, 20, 40]
# vals.pop(2)
# print(vals)

# items = ["apple", "banana", "cherry"]
# items.insert(1, "mango")
# print(items)
# print(items.index("cherry"))

#Lecture_four-sets & dictionary :

# student = {
#     "name" : "Saksham",
#     "age" : 18,
#     "subjects" : {
#         "math" : 79,
#         "science" : 78,
#         "english" : 93
#     }
# }
# science_marks = student.get("subjects").get("science")
# print(science_marks)

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.union(set2))
# print(set1.intersection(set2))

# my_set = {1, 2, 3}
# my_set.add(4)
# my_set.discard(5)
# print(my_set)
