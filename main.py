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



class Player:
    def __init__(self, name, age):
        self.age = age
    def say_hello(self):
        print("hello there")

player1 = Player('seongjin', 27)
player1.say_hello() # hello there