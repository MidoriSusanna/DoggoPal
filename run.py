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
        self.food = randrange(self.food_max)  #dog initial state of hunger
        self.excitement = randrange(self.excitement_max)  #dog initial state of excitement
        self.bath = randrange(self.bath_max)
        self.vocab = self.vocab[:]

    def __clock_tick(self):  #simulate the passage of time, food excitment and bath decrease
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
    

    def teach(self, word):
        """Teach a command to the dog"""
        self.vocab.append(word)
        self.__clock_tick()
    

    def talk(self):
        """Dog introduce itself"""
        print(f"I am a {self.dog_breed} named {self.name}. {self.description()}")
        print(self.vocab[randrange(len(self.vocab))])
        self.__clock_tick()
    

    def feed(self):
        """Feeding the dog"""
        print("It's delicious! Thank you (っ ᵔ◡ᵔ)っ")
        meal = randrange(0, self.food_max)
        self.food += meal

        if self.food < 0:
            self.food = 0
            print("Please feed me more.")
        elif self.food > self.food_max:
            self.food = self.food_max
            print("Thank you. I am full!")
        self.__clock_tick()
    

    def play(self):
        """Make the dog play"""
        print("Let's Play! Woof!")
        fun = randrange(0, self.excitement_max)
        self.excitement += fun
        if self.excitement < 0:
            self.excitement = 0
            print("I am sad and bored...(｡T ω T｡)")
        elif self.excitement > self.excitement_max:
            self.excitement = self.excitement_max
            print("I am so happy when you play with me! (´♡‿♡`)")
        self.__clock_tick()
    
    
    def wash(self):
        """Give the dog a bath"""
        print("I do not like baths...")
        shower = randrange(0, self.bath_max)
        self.bath += shower
        if self.bath < 0:
            self.bath = 0
            print("I rolled in the mud (>ω^)")
        elif self.bath > self.bath_max:
            self.bath = self.bath_max
            print("Now I am fresh and clean (☆▽☆)")
        self.__clock_tick()


def main():
    dog_name = input("What is the name of your pet?")
    chosen_breed = input("What breed is your dog? /Type a breed or 'mixed-breed'.")
    #Create the dog to play with
    my_dog = Dog(dog_name, chosen_breed)

    input(
        "Woof! My name is " +
        my_dog.name +
        " and I am a/an " +
        my_dog.dog_breed + "." +
        "\n Press enter to play."
    )

    choice = None

    while choice != 0:
        print("\n PLAY WITH DOGGOPAL")
        print("1 - Feed your dog")
        print("2 - Talk with your dog")
        print("3 - Teach your dog a command")
        print("4 - Play with your dog")
        print("5 - Give your dog a bath")
        print("0 - Go to sleep \n")
        choice = input("Choose what to do with your dog: ")
        
        if choice == "0":
            print("Goodnight")
        elif choice == "1":
            my_dog.feed()
        elif choice == "2":
            my_dog.talk()
        elif choice == "3":
            new_command = input("What command would you like to teach your dog?")
            my_dog.teach(new_command)
        elif choice == "4":
            my_dog.play()
        elif choice == "5":
            my_dog.wash()
        else:
            print("Please input a valid option.")


main()
    
