class employe:
    def __init__(self):
        self.emponame="ron" #public
        self._empoage=22    #_protected
        self.__salary=23000 #__private

emp=employe()
print(emp.emponame)
print(emp._employe__salary)
