# CMPT 120 Intro to Programming
# Lab #7 – Lists and Error Handling
# Author: Vincent Manna
# Created: 2020-04-26


symbol = [" ", "x", "o"]


def printRow(row):
    row = ['_'] * 9
    pass


theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}


def printBoard(row):
    print('+--------+')
    print('|' + row['7'] + ' |' + row['8'] + ' |' + row['9'] + ' |')
    print('+--------+')
    print('|' + row['4'] + ' |' + row['5'] + ' |' + row['6'] + ' |')
    print('+--------+')
    print('|' + row['1'] + ' |' + row['2'] + ' |' + row['3'] + ' |')
    print('+--------+')
    pass


def markBoard(row, col):
    if theBoard[move] == ' ':
        theBoard[move] = xo
        count += 1
    else:
        print("That spot is taken.\nTry another spot.")
    pass


def getPlayerMove():
    move = ' '
    while True:
        if move not in '1 2 3 4 5 6 7 8 9'.split():
            print('Where is your next move? (Choose 1-9)')
            move = input()
            return int(move)


def hasBlanks(board):
    for key in theBoard:
        board_keys.append(key)

    # if so, return True
    return True


def main():
    xo = symbol[1]

    for i in range(100):
        printBoard(theBoard)
        print("Player 1 is X -- Player 2 is O \nPlayer 1 goes first!")
        print("Turn:", xo, ". Which place?")

        move = input()

        if theBoard[move] == symbol[0]:
            theBoard[move] = xo

        else:
            print("That spot is taken.\nTry another spot.")
            continue

        if xo == symbol[1]:
            xo = symbol[2]
        else:
            xo = symbol[1]


main()


