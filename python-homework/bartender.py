# 028 Feladat: Vezérlési szerkezetek gyakorlása
# A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható el a megoldás.
#
# Kérd be a felhasználó életkorát, és kérdezd meg, mit iszik. Kétféle italt ismerünk: sör és kóla. Ha a felhasználó kiskorú, és sört kér, akkor közöld vele, hogy sajnos nem adhatsz neki. Ha a felhasználó 60 feletti, és kólát kér, akkor közöld vele, hogy a koffein megemelheti a vérnyomását. Ha ismeretlen italt adott meg, akkor írd ki, hogy csak sört és kólát tudunk adni. Minden más esetben szolgáld ki. (Írd ki pl. "Parancsoljon, a söre." vagy "Parancsoljon,a kólája.")
# A megoldást egy bartender.py nevű file-ban kell beadnod.
#
# Feladat beadása
# A fent eméített python file-okat és benne a megoldásodat kérlek a saját selenium-py-peldatar github repo forkodban egy python-homework nevű mappába helyezd el.

age = input("Kérem, adja meg életkorát:")
if int(age) <= 0 or int(age) > 110:
    print(input("Kérem, adja meg életkorát számmal!"))

drink = input("Kérem, válasszon italt, sört vagy kólát:")

if int(age) < 18 and str(drink) == "sör":
    print("18 éven aluliaknak nem szolgálunk fel sört!")
elif int(age) > 60 and drink == "kóla":
    print("A koffein megemelheti a vérnyomását!")
elif drink != "sör" and drink != "kóla":
    print("Csak sör és kóla választható!")
else:
    print(f"Parancsoljon a kért ital: {drink}!")

# while int(age) <= 0 or int(age) > 110:
    #     print(input("Kérem, adja meg életkorát számmal!"))
    #     if 0 < int(age) < 110:
    #         continue
