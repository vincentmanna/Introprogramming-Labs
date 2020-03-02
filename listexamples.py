colors = 'RED', 'BLUE', 'GREEN', 'ORANGE', 'PURPLE', 'YELLOW', 'VIOLET'


def func():
    global colors
    global showTitle
    global praiseuser
    global ridiculeUser
    global confirmColor
    global containsElement


def showTitle():
    print('Color Preference Evaluator')
    global promptForColor


def promptForColor():
    global xx
    xx = input('Guess a color on the rainbow! ').upper().strip()


def confirmColor():
    uen = 'You entered: '
    print(uen, xx)
    global qq
    qq = input('Is this correct (y/n)? ')
    while True:
        if qq == 'y':
            print('Color confirmed!')
            break
        else:
            main()


def containsElement():
    global colors
    while True:
        if xx == colors[0]:
            praiseUser()
            break
        else:
            ridiculeUser()
            break


def praiseUser():
    print('Good job! You guessed correct!')


def ridiculeUser():
    print('Darn! That is incorrect!')


def main():
    a = showTitle()
    b = promptForColor()
    c = confirmColor()
    d = containsElement()


main()


