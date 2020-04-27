# CMPT 120 Intro to Programming
# Lab #7 – Lists and Error Handling
# Author: Vincent Manna
# Created: 2020-04-26

class Product:

    def __init__(self, name, price, quant):
        self.name = name
        self.price = productPrices
        self.quantity = quantity

    def instock(self):
        print(int(productQuantities.quantity))

    def cost(self):
        print(productPrices.price)


p = Product()
p.cost

productNames = ["Ultrasonic range finder"
    , "servo motor"
    , "servo controller"
    , "microcontroller Board"
    , "laser range finder"
    , "ithium polymer battery"
                ]
productPrices = [2.50, 14.99, 44.95, 34.95, 149.99, 8.99]
productQuantities = [4, 10, 5, 7, 2, 8]


def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0, len(productNames)):
        if productQuantities[i] > 0:
            print(str(i) + ")", productNames[i], "$", productPrices[i])
            print()


def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()
        vals = input("Enter product ID and quantity you wish to buy:").split(" ")
        if vals == "quit": break


main()
