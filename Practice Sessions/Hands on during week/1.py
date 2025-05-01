#Define some variable
"""
A = "Lakmali"
B = 10
print("Value of A is", A)
print("Value of B is", B)
C = type(A)
D = type(B)
print("Type of A is",C)
print("Type of B is",D)

X = "Banana","Apple","Mango"
print("values are",X)
Y ,Z = "Orange", "Blue"
print("Color 1 is",Y)
print("Color 2 is",Z)

#Fruits_I_Like = [["Orange": "Orange color"],["Apple": "red color"],["Guava": "Green color"]]
Fruits_I_Like = [["Orange", "Orange color"],["Apple", "Red color"],["Guava", "Green color"]]
XX = Fruits_I_Like[0]
YY = Fruits_I_Like[1]
ZZ = Fruits_I_Like[2]
print ("test fruit YY is",YY[0])
print ("test fruit YY COLOR IS is",YY[1])
"""

class vehicle:
    def __init__(self,make,color):
        self.make = make
        self.colo = color
    
    def input (self):
        make = input("Enter value for make")
        color= input ("Enter value for color")
        print("color is",self.color," and make is ", self.make)

Mazda = vehicle()
Mazda.input()