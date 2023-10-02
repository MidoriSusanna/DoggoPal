from random import randrange
from time import sleep
import sys
import time


# Dog pet class
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
    vocab = ["Woof, Woof!"]

    def __init__(self, name, dog_breed, dog_age):
        # Initialize the dog with a name, breed, and age
        self.name = name
        self.dog_breed = dog_breed
        self.dog_age = dog_age
        # dog initial state of hunger
        self.food = randrange(self.food_max)
        # dog initial state of excitement
        self.excitement = randrange(self.excitement_max)
        # dog initial state of being clean
        self.bath = randrange(self.bath_max)
        self.vocab = self.vocab[:]
        self.commands = {}

    def __clock_tick(self):
        """Simulate the passage of time:
        food, excitment and bath decrement (attributes)"""
        self.excitement -= 1
        self.food -= 1
        self.bath -= 1

    def description(self):
        """Describe the dog's behavior
        based on its state"""
        if (self.food > self.food_warning and
            self.excitement > self.excitement_warning and
            self.bath > self.bath_warning):
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
        """Teach a word to the dog and decrement
        food, excitement and bath"""
        self.vocab.append(word)
        self.__clock_tick()

    def talk(self):
        """Dog introduces itself
        and decrement attributes"""
        slow_typing(f"I am a {self.dog_breed}"
                    f"named {self.name}. {self.description()}")
        sleep(1)
        slow_typing(self.vocab[randrange(len(self.vocab))])
        self.__clock_tick()    

    def feed(self):
        """Feed the dog, the function
        updates the food level and decrement
        attributes"""
        slow_typing("It's delicious! Thank you (っ ᵔ◡ᵔ)っ")
        meal = randrange(0, self.food_max)
        self.food += meal

        if self.food < 0:
            self.food = 0
            slow_typing("Please feed me more.")
        elif self.food > self.food_max:
            self.food = self.food_max
            slow_typing("Thank you. I am full!")
        self.__clock_tick()

    def play(self):
        """Make the dog play, the function
        updates the excitement level and decrement
        attributes"""
        slow_typing("Let's Play! Woof!")
        fun = randrange(0, self.excitement_max)
        self.excitement += fun
        if self.excitement < 0:
            self.excitement = 0
            slow_typing("I am sad and bored...(｡T ω T｡)")
        elif self.excitement > self.excitement_max:
            self.excitement = self.excitement_max
            slow_typing("I am so happy when you play with me! (´♡‿♡`)")
        self.__clock_tick()

    def wash(self):
        """Give the dog a bath, the function
        updates the being clean level and decrement
        attributes"""
        slow_typing("I do not like baths...")
        shower = randrange(0, self.bath_max)
        self.bath += shower
        if self.bath < 0:
            self.bath = 0
            slow_typing("I rolled in the mud (>ω^)")
        elif self.bath > self.bath_max:
            self.bath = self.bath_max
            slow_typing("Now I am fresh and clean (☆▽☆)")
        self.__clock_tick()

    def command_learn(self):
        """Teach the dog a command,
        update the command count, and decrement
        attributes"""
        slow_typing(f"To learn a command,"
                    f"{self.name} needs to practice 3 times.")
        sleep(1)
        slow_typing(f"Be patient. Input the command 3"
                    f"times during the game to make {self.name} learn.")
        sleep(1)
        learn_command = no_empty_string("What command would"
                                        "you like to teach"
                                        "your dog?\n").lower()
        if learn_command in self.commands:
            self.commands[learn_command] += 1

            if self.commands[learn_command] >= 3:
                slow_typing(f"I have learnt the command:"
                            f"'{learn_command}'! Thank you!")
                self.commands[learn_command] = 3
            else:
                slow_typing(f"I am trying to learn"
                            f"the command: '{learn_command}'..."
                            f"Please keep teaching me.")
        else:
            self.commands[learn_command] = 1
            slow_typing(f"I am trying to learn"
                        f"the command: '{learn_command}'..."
                        "Please keep teaching me.")
        self.__clock_tick()

    def go_walk(self):
        """Go for a walk with your dog
        according to its age, decrement
        attributes"""
        if self.dog_age == "A":
            slow_typing("Please bring me out for a walk."
                        "I want to run, play, explore!")
        elif self.dog_age == "B":
            slow_typing("Let's go to the park and meet dog friends!")
        else:
            slow_typing("I feel tired. Let's rest together on the couch.")
        self.__clock_tick()          


def no_empty_string(prompt):
    """Function to avoid empty or blank
    strings as input"""
    while True:
        user_input = input(prompt)
        # stripping white spaces to check if the string is empty
        if user_input.strip():
            return user_input
        else:
            print("\nThe input cannot be empty. Please enter a valid input.")


def dog_age_input(prompt):
    """Validate dog age by giving
     only three options to choose between"""
    while True:
        user_input = input(prompt).strip().upper()
        if user_input in ('A', 'B', 'C'):
            return user_input
        else:
            print("Please input a valid option. Enter 'A', 'B' or 'C'.")


def slow_typing(text, delay=0.03):
    """Function to make a typing effect"""
    for ltr in text:
        sys.stdout.write(ltr)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def main():
    """Main function - Start Game"""
    slow_typing("Hi! This is DoggoPal, your virtual best friend. U・ᴥ・U\n")
    sleep(1)
    slow_typing("Answer the following questions to play with me"
                "and be my friend for today.\n")
    sleep(2)
    dog_name = no_empty_string("What is the name of your dog?\n")
    chosen_breed = no_empty_string("What breed is your dog?\n")
    dog_age = dog_age_input("Is your dog: A - a puppy,"
                            "B - a young dog, C - an older dog?")
    # Create the dog to play with
    my_dog = Dog(dog_name, chosen_breed, dog_age)

    input(
        "\nWoof! My name is " +
        my_dog.name +
        " and I am a/an " +
        my_dog.dog_breed + "." +
        "\n Press enter to play."
    )

    choice = None

    while choice != 0:
        # Set game environment
        sleep(3)
        print("\n PLAY WITH DOGGOPAL")
        print("1 - Feed your dog")
        print("2 - Talk with your dog")
        print("3 - Teach your dog a word")
        print("4 - Play with your dog")
        print("5 - Give your dog a bath")
        print("6 - Teach your dog a command")
        print("7 - Go for a walk")
        print("0 - Go to sleep \n")
        choice = input("Choose what to do with your dog: ")

        if choice == "0":
            sleep(2)
            slow_typing("Goodnight, hopefully I will see you tomorrow.")
            break
        elif choice == "1":
            sleep(2)
            my_dog.feed()
        elif choice == "2":
            sleep(2)
            my_dog.talk()
        elif choice == "3":
            sleep(2)
            new_word = no_empty_string("What word would you like"
                                       "to teach your dog?\n")
            my_dog.teach(new_word)
        elif choice == "4":
            sleep(2)
            my_dog.play()
        elif choice == "5":
            sleep(2)
            my_dog.wash()
        elif choice == "6":
            sleep(2)
            my_dog.command_learn()
        elif choice == "7":
            sleep(2)
            my_dog.go_walk()
        else:
            print("Please input a valid option.")


main()
