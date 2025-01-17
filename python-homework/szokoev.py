# Feladat: Python függvények gyakorlása
# A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható el a megoldás.
#
# Szökőév?
# Készíts függvényt, amelyik adott évszámról eldönti, hogy az szökőév-e. Szökőév minden negyedik, nem szökőév minden századik, mégis az minden 400-adik. (2000-ben ezért volt szökőév.) A függvény visszatérési értéke legyen logikai típusú! Tipp( % maradekos osztas operátor)
# Írj programot, amelyik a felhasználótól évszámokat kér, és mindegyikre kiírja, hogy szökőév-e! Használd az előbb megírt függvényt! Például: ? 2005 Nem szökőév. ? 2000 Szökőév. ? 1980 Szökőév. ? 1900 Nem szökőév.
# A megoldást egy szokoev.py nevű file-ban kell beadnod.
#
# Feladat beadása
# A fent eméített python file-okat és benne a megoldásodat kérlek a saját selenium-py-peldatar github repo forkodban egy python-homework nevű mappába helyezd el.

# függvénnyel
print("A program megállapítja egy évszámról, hogy szökőév-e:")
year = int(input("Adjon meg egy évszámot:"))

def leap_year(a):
    if year % 400 == 0:
        print(str(year) + " szökőév.")
    elif year % 100 == 0 and year % 4 == 0:
        print(str(year) + " nem szökőév.")
    elif year % 100 != 0 and year % 4 == 0:
        print(str(year) + " szökőév.")
    else:
        print(str(year) + " nem szökőév.")

leap_year(year)

# nem függvénnyel:
# print("A program megállapítja egy évszámról, hogy szökőév-e:")
# year = input("Adjon meg egy évszámot:")
#
# if (int(year) % 4) == 0:
#     if (int(year) % 100) == 0:
#         if (int(year) % 400) == 0:
#             print(str(year) + " szökőév.")
#         else:
#             print(str(year) + " nem szökőév.")
#     else:
#         print(str(year) + " szökőév.")
# else:
#     print(str(year) + " nem szökőév.")