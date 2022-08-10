from abc import ABC , abstractmethod
  
class Polygon(ABC):   
  
   # abstract method 
    @abstractmethod  
    def sides(self):   
        pass  
    
    # @abstractmethod
    # def length(self):
    #     ...
        
    def normal_func(self):
        print("this is normal func")
  
  
# TypeError: because we can't instantiate an object for abstract class
# pol = Polygon()     
  
class Triangle(Polygon):   
     
    def sides(self):   
        print("Triangle has 3 sides") 
      
    def another_func(self):
        print("this is another func")  

class Pentagon(Polygon):   
     
   def sides(self):   
      print("Pentagon has 5 sides")   
      
t = Triangle()   
t.sides()
t.normal_func() 
t.another_func()  

p = Pentagon()   
p.sides()   

class Car(ABC):
    
    @abstractmethod
    def test_drive(self):
        ...   
        
    @abstractmethod
    def next_method(self):
        ...
    
# c = Car() #Error: can't instantiate an abstract class
    
class BMW(Car):
    
    def test_drive(self):
        print("Its BMW driving")
        
    # If you inherit an abstract class, you have to provide implementations to all the abstract methods in it.
    # Else, you cannot instantiate the subclass too
    
    def next_method(self):
        print('this is another abstract method overriden in subclass')

bmw = BMW()
bmw.test_drive()
bmw.next_method()
