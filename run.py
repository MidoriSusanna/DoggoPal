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
    cuddle_reduce = 3
    cuddle_max = 10
    cuddle_warning = 3
    vocab = ['"Woof, Woof!"']

    def __init__(self, name, dog_breed):
        self.name = name
        self.dog_breed = dog_breed
        self.food = randrange(self.food_max) #dog initial state of hunger 
        self.excitement = randrange(self.excitement_max) #dog initial state of excitement
        self.vocab = self.vocab[:]