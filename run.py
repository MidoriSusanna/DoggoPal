# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from random import randrange

#Dog pet class
class Dog(object):
    """
    A virtual dog to play with and look after
    """
    excitement_reduce = 3
    excitement_max = 10
    excitement_warning = 3
    food_reduce = 2
    food_max = 10
    food_warning = 3
    bath_reduce = 3
    bath_max = 10
    bath_warning = 3
    vocab = ['"Woof, Woof!"']

    def __init__(self, name, dog_breed):
        self.name = name
        self.dog_breed = dog_breed
        self.food = randrange(self.food_max)#dog initial state of hunger
        self.excitement = randrange(self.excitement_max)#dog initial state of excitement
        self.bath = randrange(self.bath_max)
        self.vocab = self.vocab[:]

    def __clock_tick(self): #simulate the passage of time, food excitment and bath decrease
        self.excitement -=1
        self.food -=1
        self.bath -=1
    
    def description(self):
        """ Dog behaviour"""
        if self.food > self.food_warning and self.excitement > self.excitement_warning and self.bath > self.bath_warning:
            return f"{self.name} doggo is happy! *wiggles tale* (´♡‿♡`)"
        elif self.food < self.food_warning:
            return f"{self.name} doggo is hungry (＞﹏＜)"
        elif self.excitement < self.excitement_warning:
            return f"{self.name} doggo is sad and bored... (｡T ω T｡)"
        elif self.bath < self.bath_warning:
            return f"{self.name} doggo is stinky... (￣▽￣*)ゞ"
        else:
            return f"{self.name} doggo is quiet... (*＾ω＾)人(＾ω＾*)"