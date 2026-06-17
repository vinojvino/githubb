status= 700

match status:
    case 200:
        print("ok")
    case 500:
        print("not ok")
    case 400:
        print("very ok")
    case _:
        print("good")

        
word_count={}
chare="hello,darkness"
for n in chare:
    if n in word_count:
        word_count[n]=word_count[n]+1
    else:
        word_count[n]=1
print(word_count)
