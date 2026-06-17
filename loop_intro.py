#list
"""fruits={10:"apple",10.5:"orange"}
for fruit in fruits:
    print(fruit)

for num in range(1,10):
    print(num)

i=list(range(100,9,-10))
print(i)"""
     #range
# i=dict(range('a':100,'b':9))
# print(i)

     #loop
# numb=[2,8,12,22]
# total=0
# for n in numb:
#     total=total+n
#     print(total)

#even numb
#num=[1,2,3,4,5,6,7,8,9]
# for n in num:
#     if n%2==0:
#         print(n)

#even numbers

# for looop

"""count=int(input("enter the count:"))
number=[]
for c in range(count):
    c=int(input("enter the numbers:"))
    number=number+[c]
for j in number:
    if j%2==0:
        print(j)"""

'''
count=1
while count<=10:
    print(count,end="0")
    count+=1'''

'''for k in range(1,6):
    for n in range(1,k+1):
        print(n,end=" ")
    print(" ")'''
'''
for k in range(1,6,):
    for sp in range(5-k):
        print(" ",end=" ")
    for c in range(1,k+1):
        print("*",end=" ")
    print(" ")
    '''
"""for r in range(1,6):
    num=r
    for c in range(r):
        print(num,end=" ")
        num+=r
    print("") 
"""

'''for r in range(1,5):
    num=r
    for c in range(r):
        print(c)'''

'''for k in range(6):
    for sp in range(5-k):
        print(" ",end=" ")
    for c in range(1,k+1):
        print("*",end=" ")
    print(" ")'''

'''k,s=1,2
s=3
print(k,s,end="s")
print(s)'''
'''first,second=0,1
print(first,second,end=" ")
count=1
while count<=8:
    third=first+second
    print(third,end=" ")
    first,second=second,third
    count+=1'''

'''word_count={}
char=("hello","darkness","hello")
for c in char:
    for n in c:
        if n in word_count:
            word_count[n]=word_count[n]+1
        else:
            word_count[n]=1
print(word_count)
'''

for item in ("apple", "banana"):
    print(item)