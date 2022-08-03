from random import randint

class Employee:
    def __init__(self, emp_code, name):
        self.emp_code = emp_code
        self.name = name
        
    @staticmethod
    def generate_emp_code():
        value = randint(1000, 9999)
        return value
        
    @classmethod
    def create_emp_by_empcode(cls, name):
        code = cls.generate_emp_code()
        return cls(code, name)  #this is creating object of the class itsself
        
        
e = Employee("ABc", 1234)
e1 = Employee.create_emp_by_empcode('liza')

print(e.name, e.emp_code)

print(e1.name, e1.emp_code)