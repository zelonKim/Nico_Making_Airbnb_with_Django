""" 
class Player:
    def __init__(self):
        self.age = 27

seongjin = Player()
print(seongjin.age) # 27 
"""



""" 
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

player1 = Player('seongjin', 27)
print(player1.name) # seongjin
print(player1.age) # 27  
"""


####################################



"""
 class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"hello {self.name}")



class Fan:
    def __init__(self, name, fav_team):
        self.name = name
        self.fav_team = fav_team

    def say_hello(self):
        print(f"hello {self.name}")     


player1 = Player("nico", 10)
player1.say_hello() 

fan1 = Fan("seongjin", "nomad")
fan1.say_hello()  
 """



################

""" 
class Human:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print(f"hello {self.name}")



class Player(Human):
    def __init__(self, name, age):
        self.age = age
    

class Fan(Human):
    def __init__(self, name, fav_team):
        self.fav_team = fav_team



player1 = Player("nico", 10)
player1.say_hello()

fan1 = Fan("seongjin", "nomad")
fan1.say_hello()
 """

 #########################


""" class Human:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print(f"hello {self.name}")


class Player(Human):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    

class Fan(Human):
    def __init__(self, name, fav_team):
        super().__init__(name)
        self.fav_team = fav_team



player1 = Player("nico", 10)
player1.say_hello()

fan1 = Fan("seongjin", "nomad")
fan1.say_hello() """


##########################

""" class Dog:
    def woof(self):
        print('woooooof')

class Beagle(Dog):
    def sing(self):
        super().woof()
        print('jump')

beagle = Beagle()
beagle.sing() # woooooof  # jump """

########################


""" 
class Dog:
    def woof(self):
        print('woooooof')

class Beagle(Dog):
    def woof(self):
        super().woof()
        print('jump')

beagle = Beagle()
beagle.woof() # woooooof # jump 
"""

####################


"""
 class Dog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "hahaha"

dog1 = Dog('choco')
print(dog1) # hahaha
print(dog1.name) # choco 
"""


###################


class Dog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Dog`s name: {self.name}"
    def __getattribute__(self, attr):
        return f"the attribute is {attr}"


dog1 = Dog('choco')
print(dog1.age) # the attribute is age
