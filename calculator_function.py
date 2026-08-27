print("---Calculator2.0--->")
print()
def calc_sum(a, b):
    sum = a+b
    return sum
def calc_minus(a, b):
    minus = a-b
    return minus
def calc_prod(a, b):
    prod = a*b
    return prod
def calc_div(a, b):
    if(b == 0):
        print(a,"/",b,"= Undefined")
    else:
        print(a,"/",b,"=",a/b)
def calc_mod(a, b):
    if(b==0):
        print(a,"%",b,"= Undefined")
    else:
        print(a,"%",b,"=", a%b)

num1 = int(input("Enter 1st number : "))
opr = input("Enter operator : ")
num2 = int(input("Enter 2nd number : "))

if(opr == "+"):
    print(num1,"+",num2,"=", calc_sum(num1, num2))
elif(opr == "-"):
    print(num1,"-",num2,"=", calc_minus(num1, num2))
elif(opr == "*"):
    print(num1,"*",num2,"=", calc_prod(num1, num2))
elif(opr == "/"):
    calc_div(num1, num2)
elif(opr == "%"):
    calc_mod(num1, num2)
else:
    print("Invalid operation")
