
class Person:
    def __init__(self, name):
        self.name = name
        self.is_emp = False
        
    def get_description(self):
        print("This is a person class description.", self.name, self.is_emp)
    
# single inheritance
    
class Employee(Person):
    
    def employee_status(self):
        self.is_emp = True
        
        
person = Person("ABC")
print("person", person.name, person.is_emp)
print("person parent class calling method", person.get_description())

employee = Employee("liza")
employee.employee_status()
print("employee", employee.name, employee.is_emp)
print("employee classs calling parent method")
employee.get_description() 


# When a parent class is inherited by more than one child or subclasses -> Hierarchial Inheritance
class Staff(Person):
    
    # Overriding init example
    def __init__(self, name):
        super(Staff, self).__init__(name)
        self.is_emp = True

    def get_staff_status(self):
        
        return self.is_emp

staff_obj = Staff("liza")
print("Staff", staff_obj.name, staff_obj.is_emp)
print("get staff status", staff_obj.get_staff_status())
staff_obj.get_description()


class Dog:
    def __init__(self, name, color):
       self.name = name
       self.color = color
    
    def get_color(self):
        print("Parent class:", self.color)
        
        return self.color

class Labrador(Dog):
    
    def __init__(self, name, color, fur="double-coated"):
        super(Labrador, self).__init__(name, color)
        self.fur = fur
        
        
dog = Dog('Tom','black')
lab_obj = Labrador('Mickey', "golden")

print(dog.name, dog.color)
print(lab_obj.name, lab_obj.color, lab_obj.fur)
print(lab_obj.get_color())
print(dog.get_color())
# print(dog.fur)           # >> Error coz parent class has no breed_name

# Classwork: Do for Vehicle with parameters brand, model and num of wheels. 
# Inherit it to Car and Bike, override the num of wheels attribute for car and bike respectively. 
