
# Operator overloading

print(3+5)
print("3"+"ab")

# Polymorphism with functions and objects --> Method overloading

class Area:
    def find_area(self, a=None, b=None):
        if a != None and b != None:
            print("Rectangle:", (a * b))
        elif a != None:
            print("square:", (a * a))
        else:
            print("No figure assigned")
obj1=Area()
obj1.find_area()
obj1.find_area(10)
obj1.find_area(10,20)


# Next example of method overloading:
class Tomato(): 
    def type(self): 
        print("Vegetable") 
    def color(self):
        print("Red") 
       
class Apple(): 
    def type(self): 
        print("Fruit") 
    def color(self): 
        print("Red") 
      
def func(obj): 
       obj.type() 
       obj.color()
        
obj_tomato = Tomato() 
obj_apple = Apple() 
func(obj_tomato) 
func(obj_apple)


# Method overriding in inheritance


class Bird:
    def intro(self):
        print("There are many types of birds.")
        
    def flight(self):
        print("Most of the birds can fly but some cannot.")
   
class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")
     
class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")
     
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
 
obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()