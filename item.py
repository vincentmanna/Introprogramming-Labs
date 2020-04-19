# CMPT 120 Intro to Programming
# Lab 8
# Author: Vincent Manna
# Created: 2020-04-19

class item:
    item = 'flashlight'
    description = 'a device that shines light into a directed spot.'

    def render(self):
        print(item.description)


it = item()
it.render()


def containsitem():
    lablist = ['flashlight', 'lamp', 'table', 'desk']
    search = 'flashlight'
    result = [i for i in lablist if search in i]
    print('The string searched for is: ' + str(result))


containsitem()











