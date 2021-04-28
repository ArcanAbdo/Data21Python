import random
from hangman_functions import name_input

name = name_input()


def hangmangame():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
               "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
               "u", "v", "w", "x", "y", "z"]
    letters_guessed = []
    word_list = ['Word', 'another', 'other', 'something']
    lives = 8
    hangman_word = random.choice(word_list)
    hangman_word = hangman_word.lower()
    out_list = []
    play_again_boolean = True

    for characters in hangman_word:
        print("_", end="")
    print(f"\nThis word is {len(hangman_word)} letters long")

    while lives != 0:
        if "".join(out_list) == hangman_word:
            play_again = input("Congratulations!!!! You have successfully saved a life, Would you like to play again?\n")
            play_again = play_again.lower()
            while "".join(out_list) == hangman_word:
                play_again = input()
                if play_again in ["no", "n", "0"]:
                    break
                elif play_again in ["yes", "y", "1"]:
                    hangmangame()
                else:
                    print("I'm sorry, I didn't understand that. Would you like to play again?")
        guess = input("\nGuess a letter of the alphabet? \n")
        guess = guess.lower()
        letters_guessed.append(guess)
        if guess in hangman_word:
            letters.remove(guess)
            print(f"Yes you're right! {guess} is in the word!")
            out_list = []
            for characters in hangman_word:
                if characters in letters_guessed:
                    out_list.append(characters)
                elif characters != guess:
                    out_list.append("_")
            print("".join(out_list))
        else:
            letters_guessed.append(guess)
            letters.remove(guess)
            print(f"ooh, incorrect I'm afraid. {guess} was not in the word \n")
            lives = lives - 1
            print(f"You have {lives} guesses remaining")
    print("You are out of chances I'm afraid.")
    play_again = input("Would you like to play again?\n")
    play_again = play_again.lower()
    while play_again_boolean:
        if play_again in ["yes", "y", "1"]:
            hangmangame()
        elif play_again in ["no", "n", "0"]:
            break
        else:
            print("I'm sorry. I didn't understand that. Would you like to play again?")


hangmangame()
