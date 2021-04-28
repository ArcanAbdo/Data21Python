# if divisible by 3 fizz, divisible by 5 buzz, fizzbuzz divisible by both

number_start = int(input("What number do you want to start at? \n"))
number_end = int(input("What number do you want to end at? \n")) + 1
r = list(range(number_start, number_end, 1))
for num in r:
    if num % 5 == 0 and num % 3 == 0:
        print("FIZZBUZZ")
    elif num % 3 == 0:
        print("FIZZ")
    elif num % 5 == 0:
        print("BUZZ")
    else:
        print(num)
