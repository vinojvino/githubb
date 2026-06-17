"""age=int(input("enter your age : "))
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible")"""


a=int(input("enter num1 : "))
b=int(input("enter num2 : "))
print("1.addition\n2.substraction\n3.multiplication\n4.division")
operation=int(input("enter your number:"))
if operation==1:
    result=(a+b)
    print(f"result:{a} + {b} = {result}")
elif operation==2:
    result=(a-b)
    print(f"result:{a} - {b} = {result}")
elif operation==3:
    result=(a*b)
    print(f"result: {a} * {b} = {result}")
elif operation==4:
    if b !=0:
        result=(a/b)
    else:
        print("please provide valid number")
else:
    print("provide valid operator")
