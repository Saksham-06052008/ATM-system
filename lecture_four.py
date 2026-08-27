#dictionary in python

# info ={
#     "name" : "saksham",
#     "cgpa" : 8.5,
#     "age" : 18,
#     "subjects" : ["python", "coding", "DSA"]
# }

# print(type(info))
# info["cgpa"] = 9
# info["surname"] = "sharma"
# print(info)
# null_dict = {}
# null_dict["name"] = "gouri"
# print(null_dict)
# student = {
#     "name" : "saksham",
#     "subjects" : {
#         "phy" : 73,
#         "chem" : 65,
#         "maths" : 78
#     }
# }
# print(student["subjects"])
# print(list(student.values()))
# dict = {
#     "class" : 11,
#     "age" : 18,
#     "school" : "Model.H.S.S"
# }
# pairs = list(dict.items())
# print(pairs[1])
# student = {
#     "name" : "saksham",
#     "friend" : "xyz",
#     "score" : 9.3,
#     "Height" : 5.3
# }
# # print(student["friend"]) #error
# # print(student.get("friend2")
# student.update({"city" : "Morena", "age" : 18})
# print(student)

#sets in python

# joint = {1, 2, 2, 5, 6, "name", "name", "sharma"}
# print(type(joint))
# print(len(joint))# totel number of items
# collection = set()#empty set
# print(type(collection))
# collection.add(2)
# collection.add(5)
# collection.add(5)
# collection.add("saksham")
# collection.add("gouri")

# collection.remove("gouri")
# print(collection)
# collection.clear()# empties the set
# set = {"hello", "world", 2,  5, 5.3, 5}
# print(set.pop())
# set = {2, 5, 5, 1, "gouri", (4, 5, 6)}
# set2 = {1, 4, "saksham"}

# print(set.union(set2))#{2, 5, 1, 4, "gouri, "saksham , (4, 5, 6)}
# print(set.intersection(set2))

#practice question-
#1
# meaning = {
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture", "list of facts & figures"]
# }
# print(meaning)
#2
# set = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
# print(len(set))
#3
# marks = {}

# a = int(input("enter phy mark : "))
# b = int(input("enter chem mark : "))
# c = int(input("enter math mark : "))
# marks.update({"physics" : a})
# marks.update({"chemistry" : b})
# marks.update({"math" : c})
# print(marks)