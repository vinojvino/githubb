class student:
    institute="oneteam"
    def __init__(self,n,p):
        self.name=n
        self.place=p
    def display(self):
        print(f"hello you are {self.name} and you are a {self.place}")

std1=student("vinoj","kochi")
std2=student("jame","koothi")

std2.display()

class pythonstudent(student):
    def __init__(self, n, p,c):
        self.course=c
        super().__init__(n, p)
    def display(self):
        print(f"and your course is {self.course}")

std1=pythonstudent("messi","argentina","python")

std1.display()