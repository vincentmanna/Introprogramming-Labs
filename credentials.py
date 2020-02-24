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
        else:
            print("Your password is weak! Must be 8 characters or more.")
            passwd = input("Create a new password: ")

        if not any(char.isupper() for char in passwd):
            print('Password must have at least on uppercase letter')
            passwd = input("Create a new password: ")
        elif not any(char.islower() for char in passwd):
            print('Password must have at least on lowercase letter')
            passwd = input("Create a new password: ")
        else:
            print('Looks good!')
            break

    return passwd


def main():
    first, last = myname()
    print('Name: ', first, last)
    mar1, mar2 = maristname()
    print(mar1 + first.lower() + '.' + last.lower() + mar2.lower())
    passwd = mypassword()
    print('Your password is: ' + passwd)


main()

