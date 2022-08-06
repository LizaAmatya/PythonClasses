# multiple inheritance
# without super()

class First(object):
    def __init__(self):
        # super(First, self).__init__()
        print("first")
        
    # def test():
    #     print("First method")

class Second(object):
    def __init__(self):
        print("second")
        
    # def test():
    #     print("second method")

class Third(First, Second):
    def __init__(self):
        super(Third, self).__init__()     #>> yesle first ko ma jancha super() returns the next class in MRO.
        print("third")
    def test():
        print("this is 3rd method")
print("------------------------------------------")
Third()
print(Third.mro())
print(Third.test())


# with super()

class First(object):
    def __init__(self):
        super(First, self).__init__()
        print("first")
        
    # def test():
    #     print("First method")

class Second(object):
    def __init__(self):
        super(Second, self).__init__()
        print("second")
        
    def test():
        print("second method")

class Third(First, Second):
    def __init__(self):
        # super(Third, self).__init__()
        print("third")

# //error Fourth class becoz it cannot inherit the class which its parent class is already inheriting : here: second class
# class Fourth(Second, Third):
#     def __init__(self):
#         super(Fourth, self).__init__()
#         print("that's it")

# print("------------------------------------------")

# Third()
# print(Third.mro())
# print(Third.test())