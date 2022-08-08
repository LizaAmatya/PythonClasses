# hybrid - mix of different inheritances

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

# //error Fourth class becoz it cannot inherit the class
# which its parent class is already inheriting : here: second class before the third class 
# which creates a loop and has no decisive MRO to build, and throws error

# class Fourth(Second, Third):
#     def __init__(self):
#         super(Fourth, self).__init__()
#         print("that's it")
        
# print(Fourth.mro()) Fourth->Second -> Third -> First -> Second  Second class loops and throws error

# When going left to right, here: Third coomes first and Second later at last : hence no loop of class
# and doesnot throw error
class Fourth(Third, Second):
    def __init__(self):
        super(Fourth, self).__init__()
        print("that's it")
        
print(Fourth.mro())     # Fourth->Third -> First -> Second


class Fifth(Third):
    def __init__(self):
        # super(Fourth, self).__init__()
        print("Fourth class")


