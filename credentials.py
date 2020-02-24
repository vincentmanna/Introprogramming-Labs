# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Vincent Manna
# Created: 2020-02-24

def myname():
    # get user's first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return first, last


def maristname():
    mar1 = 'Your marist username is: '
    mar2 = '@marist.edu'
    return mar1, mar2


###
def mypassword():
    passwd = input("Create a new password: ")
    #  modify this to ensure the password has at least 8 characters

    while True:
        if len(passwd) >= 8:
            print("Your password is strong!")
            print("Your password is: " + passwd)
            break
        else:
            print("Your password is weak! Must be 8 characters or more.")
            passwd = input("Create a new password: ")

    return passwd


def main():
    first, last = myname()
    print(first, last)
    mar1, mar2 = maristname()
    print(mar1 + first + '.' + last + mar2)
    passwd = mypassword()
    print(passwd)


main()