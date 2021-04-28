# shopping_list = ["eggs ", "milk", "bread"]
# print(shopping_list)
# print(type(shopping_list))
# shopping_list[0] = "chocolate"
# print shopping_list

# shopping_tup = ("bread", "milk", "eggs")
# print(shopping_tup)
# Cannot change a tuple list.

# student_1 = {
#    "name": "Arcan",
#    "stream": "data21",
#    "list": ["Value1", "Value2", "Value3"]
# }
# print(student_1)
# print(student_1["stream"])
# print(student_1["list"][1])
# student_1["name"] = "Bob"
# print(student_1)

# car_parts = {"wheels", "doors", "windows"}
# print(car_parts)
# print(type(car_parts))
# car_parts.add("headlights")
# print(car_parts)
# car_parts.discard("doors")

# age = 60
# if age > 18:
#    print("You are an adult")
# if elif is used instead of another if then the action
# won't proceed. Use elif when you only need one answer.
# if age > 50:
#    print("you are old")
# else:
#    print("You are not an adult")

# list_data = [1, 2, 3, 5, 6, 7, 8, 0]
# embedded_list = [[123], [234]]
# for data in list_data:
#    print(data)
# for data2 in embedded_list:
#    print(data2)
# for data3 in embedded_list:
#    print(data3)
#    for num in data3:
#        print(num)

# x = 0
# while x < 20:
#    print("this is true")
#    print(x)
#    if x == 4:
#        break
#    x += 1

user_prompt = True

while user_prompt:
    age = input("What is your age?")
    if age.isdigit():
        user_prompt = False
    else:
        print("Digits please")