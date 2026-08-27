# def calc_sum(a, b):
#     sum = a+b
#     print(sum)
#     return sum

# calc_sum(4, 10)
# calc_sum(12, 6)

#avg of different numbers-:

# def calc_avg(a, b, c, d):
#     sum = a+b+c+d
#     avg = sum/4
#     print(avg)
#     return avg

# calc_avg(65, 93, 82, 78)

# print("Saksham sharma",end=" ")
# print("Growth")

#Lets Practice-:
# cities = ["NYC", "Roorkee", "Delhi"]
# actors = ["Brad pitt", "Ranbeer", "Chris evans", "Michel Bjorden"]
# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(actors)  

# heroes = ["Spiderman", "Batman", "Thor", "Daredevil"]

# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(heroes)


# def calc_fact(n):
#     fact = 1
#     for i in range(1 ,n+1):
#         fact = fact*i
#     print(fact)

# calc_fact(10)

# def convert(inr_val):
#     usd_val = inr_val/95
#     print(inr_val,"INR = $", usd_val)

# convert(5000000)

#<---Recursion--->

# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)

# show(5)

# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     return fact(n-1)*n

# print(fact(6))

# def sum(n):
#     if(n==0):
#         return 0
#     return sum(n-1) + n

# print(sum(6))

# def print_list(list, idx=0):
#     if(idx==len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# protein = ["Eggs", "Paneer", "Milk", "Sattu"]
# print_list(protein)
