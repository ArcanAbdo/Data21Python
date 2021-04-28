#

class AmazingDog:

    # One underscore before the variable hides the is_alive but can still be changed if known.
    # Two underscores makes it more difficult to find.
    # _is_alive = True

    # Initialisation
    def __init__(self, animal_kind):
        self.animal_kind = animal_kind
        self.bark()
        # Again, one underscore hides it but it still exists.
        # Two underscores will not
        self.__is_alive = True

    # Example of a method
    def bark(self):
        return "woof!"

    # Setter
    def set_is_alive(self, alive_status):
        self.__is_alive = alive_status

    # Getter
    def get_is_alive(self):
        return self.__is_alive

# Bob is defined within the AmazingDog class. Instantiation.
# Bob = AmazingDog("Canine")
# The print can then call it.
# print(Bob.animal_kind)

# The animal_kind for Bob, animal_kind can be changed.
# Bob.animal_kind = "dolphin"
# print(Bob.animal_kind)


Bob = AmazingDog("Canine")
# Sue = AmazingDog("Dolphin")

print(Bob.bark())
