# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3)

# f.close()

# f = open("demo.txt", "a+")
# f.write("After than i'll build few projects to publish on Github")
# print(f.read())
# f.close()

# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt", "w") as f:
#     f.write("new data")

# import os
# os.remove("demo.txt")

#PRACTICE-:

# with open("Sample.txt", "r") as f:
#     #f.write("Hi everyone\nWe are learning File I/O\nusing Java.\nI like programing in Java.")
#     data = f.read()

# new_data = data.replace("Java", "Python")
# print(new_data)

# with open("Sample.txt", "w") as f:
#     f.write(new_data)
# def check_for_word():
#     word = "learning"
#     with open("Sample.txt", "r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("Found")
#         else:
#             print("Not Found")

# check_for_word()