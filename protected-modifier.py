class Employee:
    
    def __init__(self, name, dept): 
    #  protected data members
        self._name = name
        self._department = dept
        
    # protected member function  
    def _get_dept(self):
 
        # accessing protected data members
        print("Department getting from parent class: ", self._department)
        
        return self._department
         
         
# derived class
class Manager(Employee):
         
   # protected member function
   def _display_details(self):
        # accessing protected data members from parent class
        print("Name: ", self._name)
           
        # accessing protected member functions of super class
        print("Dept:", self._get_dept())
        
 
# creating objects of the child class       
obj = Manager("Hari", "Information Technology")
 
# calling protected member functions of the class
obj._display_details()
