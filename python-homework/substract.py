# Kérjünk be két számot, és írjuk ki a különbségüket. Használd az input() és print() beépített függvényeket.
# A megoldást egy substract.py nevű file-ban kell beadnod.

num1 = int(input("Adj meg egy számot:"))
num2 = int(input("Adj meg még egy számot:"))

def substract():
    if num1 >= num2:
        num3 = num1 - num2
        print("A két szám különbsége: " + str(num3))
    else:
        num3 = num2 - num1
        print("A két szám különbsége: " + str(num3))

substract()
