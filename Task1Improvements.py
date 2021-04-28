
user_name = True
user_age = True

films = {
    "R": ["Fight Club", "Seven", "Pulp Fiction"],
    "15": ["The Shawshank Redemption", "Forrest Gump", "Saving Private Ryan"],
    "12a": ["The Dark Knight", "The Lord of the Rings", "Inception"],
    "PG": ["Spiderman - into the spiderverse", "Toy Story", "Spirited Away"],
    "U": ["12 Angry Men", "WALL-E", "The Lion King"]
}

while user_name:
    name = input("Hello. What is your name? \n")
    if name.isalpha():
        user_name = False
    else:
        print("Sorry. Your name must only contain letters of the alphabet. \n")

while user_age:
    age = input(f"Nice to meet you {name}. How old are you? \n")
    if age.isdigit():
        if int(age) >= 130:
            print("Sorry. The values are not within a valid range.")
        else:
            user_age = False
    else:
        print("Sorry. Your age must be numerical.")

if int(age) >= 18:
    print(f"As you are {age}, {name}, you can watch films rated U, PG, 12a, 15, and R")
    print(films["R"], "\n", films["15"], "\n",
          films["12a"], "\n", films["PG"], "\n",
          films["U"])
    user_prompt = False
elif 18 > int(age) >= 15:
    print(f"As you are {age}, {name}, you can watch films rated U, PG, 12a, and 15")
    print(films["15"], "\n", films["12a"], "\n",
          films["PG"], "\n", films["U"])
    user_prompt = False
elif 15 > int(age) >= 12:
    print(f"As you are {age}, {name}, you can watch films rated U, PG, and 12a")
    print(films["12a"], "\n", films["PG"], "\n",
          films["U"])
    user_prompt = False
elif 12 > int(age):
    print(f"As you are {age}, {name}, you can watch films rated U, and PG")
    print(films["PG"], "\n", films["U"])
    user_prompt = False
else:
    user_prompt = False
