# 032 Feladat: Python while ciklus gyakorlása
# A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható el a megoldás.
#
# Írj programot, mely addig olvas be számokat a billentyűzetről, ameddig azok kisebbek, mint tíz. Írja ki ezek után a beolvasott számok összegét!
# A megoldást egy tenbelow.py nevű file-ban kell beadnod.
#
# Feladat beadása
# A fent eméített python file-okat és benne a megoldásodat kérlek a saját selenium-py-peldatar github repo forkodban egy python-homework nevű mappába helyezd el.

print("10 feletti számnál a program kiírja a beírt számok összegét, majd kilép.")

number = 0
sum = 0
#
while number < 10:
    number = int(input("Válassz egy számot!:"))
    sum = sum + number

print("A beírt számok összege: " +  str(sum))
