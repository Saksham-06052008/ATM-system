print("<----Calculator---->")
print()
num1 = int(input("Enter 1st number : "))
opr = input("perform operation(+,-,*,/,%) : ")
num2 = int(input("Enter 2nd number : "))
if(opr == "+"):
    print(num1,"+",num2,"=",num1+num2)
elif(opr == "-"):
    print(num1,"-",num2,"=",num1-num2)
elif(opr == "*"):
    print(num1,"*",num2,"=",num1*num2)
elif(opr == "/"):
    if(num2 == 0):
        print(num1,"/",num2," = Undefined")
    else:
        print(num1,"/",num2,"=",num1/num2)
elif(opr == "%"):
    print(num1,"%",num2,"=",num1%num2)
else:
    print("Invalid operation")

