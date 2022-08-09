class Person:
     
    # public data member
    name = None

    # protected data member
    _age = None
    
    # private data member
    __citizenship_num = None
    
    def __init__(self, name, age, citizenship_num): 
        self.name = name
        self._age = age
        self.__citizenship_num = citizenship_num
    
# public member function  
    def display_name(self):

        # accessing public data members
        print("Public Data Member--> Name: ", self.name)
    
    # protected member function  
    def _display_protected_age(self):

        # accessing protected data members
        print("Protected Data Member --> Age: ", self._age)
    
    # private member function  
    def __display_private_citizen_num(self):

        # accessing private data members
        print("Private Data Member --> Citizenship num: ", self.__citizenship_num)

    # public member function
    def access_private_members(self):    
        
        # accessing private member function within its class only
        self.__display_private_citizen_num()

# derived class
class Employee(Person):

    # constructor
    # def __init__(self, name, age, cit_num):
    #         Person.__init__(self, name, age, cit_num)
        
    # public member function
    def access_protected_members(self):
                
            # accessing protected member functions of parent class
            self._display_protected_age()

# creating objects of the derived class    
obj = Employee("Alina", 22, "123456987")

# calling public member functions of the class
obj.display_name()
obj.access_protected_members()
obj.access_private_members()

# Object can access protected member
print("Object is accessing protected member:", obj._age)

# object can not access private member, so it will generate Attribute error
# print(obj.__citizenship_num)

# To directly access private members you can only access using its original class 
# i.e. in this case Person being parent class has the private member and not child class
print(obj._Person__citizenship_num)

#throws error
# print(obj._Employee__citizenship_num) 
