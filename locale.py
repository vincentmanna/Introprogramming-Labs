# CMPT 120 Intro to Programming
# Lab 8
# Author: Vincent Manna
# Created: 2020-04-19

class locale:
    place = 'beach'
    desc = 'The beach is beautiful. The ocean is very clear!'
    item = 'chips'

    def visit(self):
        global visit
        visit = [False]

    def render(self):
        if visit[0] == False:
            print('You arrived at the ' + locale.place)
            print(locale.desc)
        else:
            print('You have returned to the beach')

    def item(self):
        locale.item = 1
        print('You are hungry. You ate your chips')

    def removeitem(self):
        print('Chips left?')
        locale.item = None
        print(locale.item)

    def isVisited(self):
        visit[0] = True


loc = locale()
loc.visit()
loc.render()
loc.item()
loc.removeitem()
loc.isVisited()
loc.render()  # test return























