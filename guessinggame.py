def myname(gamename):
    print(gamename)


def main():
    gamename = "PYTHON GUESSING GAME"
    myname(gamename)
    print("I am thinking of a farm animal..")

    guess = input("Guess the animal I am thinking of! ")
    answer = "pig"
    x = not answer

    while guess != x:
        print("Sorry. You guessed incorrectly. Guess again..")
        guess = input("Guess the animal I am thinking of! ")

        if guess == answer:
            print("Congratulations! You guessed it!")
            break


main()