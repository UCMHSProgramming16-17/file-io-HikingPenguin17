import random

class Pokemon(object):
    
    def __init__(self, identity):
        self.name = identity
        self.level = random.randint(1, 100)
        
        
bulb = Pokemon('Bulbasaur')
char = Pokemon('Charmander')
squirt = Pokemon('Squirtle')
print(bulb.name, bulb.level)
print(char.name, char.level)
print(squirt.name, squirt.level)