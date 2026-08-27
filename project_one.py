num = int(input("Enter a Number : "))
print("<----Number Analysis---->")
print()
#positive/negative result
if(num > 0):
    print(num ,"is positive")
elif(num < 0):
    print(num ,"is negative")
else:
    print(num ,"is Zero")
#Even or Odd
if(num%2 == 0):
    print(num ,"is Even")
else:
    print(num ,"is Odd")
#table
print()
print("-Table : ")
for i in range(1 ,11):
    print(num,"*",i,"=",num*i)
#factorial
print()
print("-Factorial : ")
if(num <= 0):
    print("Please enter a Positive number")
else:
    factorial = 1
    i = 1
    for i in range(1 ,num+1):
        factorial = factorial*i
    print(factorial)
#Sum from 1 to n
print()
print("-Sum from 1 to n : ")
if(num <= 0):
    print("Please enter a Positive number")
else:
    total = 0
    i = 1
    for i in range(1 ,num+1):
        total = total+i
    print(total)
#count digits
print()
print("-Count : ")
count = 0

while num >= 1:
    num = num//10
    count = count+1
print("Number of digits = ",count)



    