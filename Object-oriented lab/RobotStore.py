from product import *

product1 = Product("Ultrasonic range finder", 2.50, 4)
product2 = Product("Servo motor", 14.99, 10)
product3 = Product("Servo controller", 44.95, 5)
product4 = Product("Microcontroller Board", 34.95 , 7)
product5 = Product("Laser range finder", 149.99, 2)
product6 = Product("Lithium polymer battery", 8.99, 8)

products = [product1, product2, product3, product4, product5, product6]

def printStock():
    print()
    print("Available Products")
    print("------------------")

    for i in range (len(products)):
        if products[i].checkStock(1):
            print(str(i)+")",products[i].name, "$", products[i].price)
            print()

def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit": break
        prodId = int(vals[0])
        count = int(vals[1])
        if products[prodId].checkStock(count):
            if cash >= products[prodId].calculateTotalPrice(count):
                products[prodId].updateQuantity(count)
                cash -= products[prodId].calculateTotalPrice(count)
                print("You purchased", count, products[prodId].name +".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else: print("Sorry, you cannot afford that product.")
        else: print("Sorry, we do not have enough of", products[prodId].name)
main()
