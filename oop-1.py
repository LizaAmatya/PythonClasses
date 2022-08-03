# class Person:
#     age = 32
#     name = "liza"
    
#     def get_name(self):
#         print(f'my name is {self.name}')
    

class Person:
    
    def __init__(self, age, name="ABC"):
        self.age = age
        self.name = name
        
    def get(self, x):
        print("calling here: ", self.name, self.age, x)
        
    def __str__(self):
        return f"My name is {self.name}"

    
p = Person(age=22)        #object person
p2 = Person(age=34, name="liza")

p3=Person(50,"Alina")


print("person", p2.name)
print('person num 3:', p3.age, p3.name)

# Calling methods
print(p.get("x is test"))         #object le afno get call garyo with its own data
print(Person.get(p2, "x is next"))      #class le get call garyo for which object vanera eg: p passes to it

print("this is str ",p2)
print("this is str for p object",p)


def get(x, y):
    pass

class Point:
    a = 5
    b = "some dtr"
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def distance_calculate(self, pointB):
        # self. x 
        # pointB.x, pointB.y  -> pointB is another point object to calculate the dist between two points
        # TODO: use distance formula sqrt((x2-x1)^2 + (y2-y1)^2) 
        pass
        

# p1 = Point(2,3)

# p2 = Point(4.5)

# p1.distance_calculate(p2)
# Point.distance_calculate(p1,p2)

print(Point.a) 

from datetime import date

class Person:
    a = 5 
    b = 6
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def normal_fun(self):
        print('this is normal fumc', self.name)
    
    @classmethod
    def obj_create_with_age_by_yr(cls, name, year):
        
        age =  date.today().year - year
        print("calculated age",age)
        
        return cls(name, age)       #this is creating anew object for the class
    
    @classmethod
    def add_vals(cls):
        res = cls.a+cls.b

        print('res')
        
        return res    
    
    @staticmethod
    def test(a,b):
        print('ajhdkjas', a, b)
        
        return "this is test"
    
person = Person("liza",22)
person.normal_fun()
# person.obj_createwithage_by_yr(Person, "this",96)     -> this gives error becoz object cannot access a classmethod

p2 = Person.obj_create_with_age_by_yr("ABC", 1998)
print(p2.age, p2.name)

print(type(person))
print(type(p2))

result = Person.add_vals()

st_res = Person.test(5, "string test")
print("type of str_res", type(st_res))

print("outisde result for static method", st_res)
    