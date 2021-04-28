# def addition(int1, int2):
#     return int1 + int2

# def division(int1: int, int2: int) -> float:
#     return int1/int2
# This will return a float. The 'int' and 'float' are there for help, not constraints.

def name_input():
    user_name = True
    while user_name:
        name = input("Hello. What is your name? \n")
        if name.isalpha():
            user_name = False
        else:
            print("Sorry. Your name must only contain letters of the alphabet. \n")
    return name


