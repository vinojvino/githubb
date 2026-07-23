"""a=("bin","can")
b=2,3,5,10
print(b)
v=("checking if changes are only made in newbranch")


for k in range(1,6):
    num=k
    for c in range(k):
        print(num,end=" ")
        num=num-1
    print(" ")"""

"""
number=6
r=101
d={}
for i in range(r):
    if number*i==number:
        d={number}
    else:
        pass

print(d)

"""

def patern(p):
    for i in range(p):
        space=" "*(p-i)
        star="*"*(2*i-1)
        print(space+star)
    
patern(20)


num=1
for i in range(1,5+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()





