"""num=7
total=0
for i in range(1,num):
    if num%i==0:
        total+=i
if total==num:
    print("yes")
else:
    print("no")"""

'''n=1
for k in range(1,6):
    num=k
    d=k-1
    for i in range(k):
        print(num,end=" ")
        num=num+d
    print(" ")'''

####word_reverse function____####
'''def word_reverse(w):
    words=w.split()
    word_reverse=words[::-1]
    c=" ".join(word_reverse)
    return c

print(word_reverse("messi is goat but ronaldo is goat"))


####prime_number____####
num=2
counter=0
limit=10

while counter<limit:
    is_prime=True
    if num==2:
        is_prime=True
    elif num<=1 or num%2==0:
        is_prime=False
    else:
        for i in range(3,int(num**0.5)+1):
            if num%i==0:
                is_prime=False

    if is_prime:
        print(num)
        counter+=1
    num+=1'''


###patern printing__###
'''for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()'''

"""def pat(n):

    for i in range(1,n+1):
        space=" "*(n-i)
        star="*"*(2*i-1)
        print(space+star,)

pat(6)"""
'''
for i in range(6):
    space=" "*(6-i)
    star="*"*(2*i-1)
    print(space+star)
'''

'''num=1
for i in range(1,5):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()'''

##prime_numbe###
'''num=2
count=0
limit=int(input("enter the number:"))
while count<limit:
    is_true=True
    if num==2:
        is_true=True
    elif num<=1 or num%2==0:
        is_true=False
    else:
        for i in range(3,num):
            if num%i==0:
                is_true=False
    if is_true:
        print(num)
        count+=1
    num+=1'''

###frequncy counter####
'''word="programming"
count_words={}
for l in word:
    if l in count_words:
        count_words[l]+=1
    else:
        count_words[l]=1

print(count_words)
'''

###perfect numbers####
'6, 28, 496,8,128'

num=7
is_perfect=True
for i in range(1,num+1):
    if num<=1:
        is_perfect=False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_perfect=True
            else:
                 print("not a perfect number")
    if is_perfect:
        print("number is perfect")
    

n=4
for i in range(n,5):
        for j in range(n):
            print("*",end=" ")
        print()
        
        







