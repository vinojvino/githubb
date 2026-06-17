'''def greet(name="user1",age=20):
    print("good morning",name)
    print("your age is",age)

greet("jame",25)

greet("son")

greet(age=23)'''


'''def total(*args):
    sum=0
    for f in args:
        sum+=f
    print(sum)

total(20,10,20)
'''
'''
def user(**kwargs):
    print("")

user(name="vinoj",age=18)'''


'''num=int(input("how many words you wish to enter:"))
words=[]
for a in range(num):
    thing=input("enter the word:")
    words=words+[thing]
print(words)

for b in words:
    if b[-1] in "aeiouAEIOU":
        print(b)
'''

'''
import math
num=5
result=math.factorial(num)
print(f"the factorial of {num} is {result}")'''
  

     #######return function##########
'''def add(a,b):
    result=a+b
    return(result)


total=add(2,5)
print(total)'''


'''def add(a,b):
    result=a+b
    return(a+b)

total=add(5,7)'''


numbers=[20,14,30,70,9]
n=len(numbers)
for i in range(n-1):
    for j in range(n-i-1):
        if numbers[j]>numbers[j+1]:
            temp=numbers[j]
            numbers[j]=numbers[j+1]
            numbers[j+1]=temp
print(numbers)


