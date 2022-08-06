class First:
    def __init__(self) -> None:
        print('this is first init')
        
    def testing_method(self):
        print("first method")
        
        
class Second(First):
    def __init__(self) -> None:
        print('this is second init')
        return "first return"
        
    def testing_method(self):
        print("second method")
        
       
class Third(Second):
    def __init__(self) -> None:
        print('this is third init')
        
    # def testing_method(self):
    #     print("third method") 
        
third = Third()

print(Third.mro())
print(third.testing_method())
    
    