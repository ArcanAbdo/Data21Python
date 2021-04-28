from animalclass import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True

    def use_venom(self):
        print("If I have venom, I am going to use it")

    def moving(self):
        print("Moves but as a snake")

    def __repr__(self):
        return f"This is a reptile"

    def __str__(self):
        return f"str version of this is a reptile"


bob = Reptile()
print(repr(bob))
print(bob)

