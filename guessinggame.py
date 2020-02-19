def myname(gamename):
    print(gamename)


def main():
    gamename = "PYTHON GUESSING GAME"
    myname(gamename)
    print("To quit the game, type any word that begins with 'q'")
    print()
    print("I am thinking of a farm animal..")
    guess = input("Guess the animal I am thinking of! ")
    answer = "pig"
    quitt = "q"
    x = not answer
    while True:
        if guess == answer:
            y = input("Congratulations! You guessed it! Do you like it? Enter 'y' or 'n'! ")
            if y == "y":
                print("I am happy you like the animal!")
                break
            elif y == "n":
                print("Thats unfortunate. I am sorry you dislike the animal!")
                break
        elif guess[0] == quitt:
            print("The game is over.")
            break
        else:
            print("You are incorrect. ")
            guess = input("Try and guess the animal again! ")


main()
