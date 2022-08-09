# public access modifier

class Counter:
    def __init__(self):
        self.current = 0

    def increment(self):
        self.current += 1

    def value(self):
        return self.current

counter = Counter()
counter.increment()
print("Public counter:", counter.value())  

# from outside the class we can modify the attribute of the class by:
counter.current = -999
print(counter.value())      


# Protected access modifier

class Counter:
    def __init__(self):
        self._current = 0

    def _increment(self):
        self._current += 1

    def _value(self):
        return self._current
    

counter = Counter()
counter._increment()
counter.current = 99    #yesto garna payena protected le garda value change hunna
counter._current = 100  #yesari protected data member lai nai access garyo vane change garn payo
print(counter._value())


# Private modifiers

class Counter:
    def __init__(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def __value(self):
        return self.__current


counter = Counter()
counter.increment()
#throws attribute error
# print(counter.__current) 
print('get counter', counter._Counter__current)
print('get value',counter._Counter__value())
