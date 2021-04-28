isogram_test = input("What word would you like to test? \n")
isogram_test = isogram_test.strip(".?!")
isogram_test = isogram_test.replace("-", "")
isogram_test = isogram_test.replace(" ", "")
isogram_test = isogram_test.lower()
print(isogram_test)

letter_boolean = True
index = 0
tally = []
while letter_boolean:
    if isogram_test[index] not in tally:
        tally.append(isogram_test[index])
        index += 1
        if index == len(isogram_test):
            print(f"{isogram_test} is an isogram")
            letter_boolean = False
    elif isogram_test[index] in tally:
        print(f"{isogram_test} is not an isogram")
        letter_boolean = False


