'''import re
text="python_123@*"
print(re.findall(r'\d',text))
print(re.findall(r'\w',text))
print(re.search('y',text))
print(re.findall(r'^py',text))
print(re.findall('@$',text))
print(re.findall(r'\W',text))'''


#####email validation#######
import re
pattern=r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email=input("enter your email:")
if re.fullmatch(pattern,email):
    print("valid email")
else:
    print("not valid")