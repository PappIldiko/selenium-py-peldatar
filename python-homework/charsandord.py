# # Feladat: Python for ciklus gyakorlása
# # A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható el a megoldás.
# #
# # rj programot, ami kiírja a kisbetűket, és melléjük az karakter kódjukat! A kiírás több oszlopos legyen, és legfeljebb 10 soros. Minta:
# # a 97 f 102 .....
# # b 98 g 103
# # c 99 h 104
# # d 100 i 105
# # e 101 j 106
# # A megoldashoz használd a beépített ord() es chr() függvényeket.
# #
# # A megoldást egy charsandord.py nevű file-ban kell beadnod.
# #
# # Feladat beadása
# # A fent eméített python file-okat és benne a megoldásodat kérlek a saját selenium-py-peldatar github repo forkodban egy python-homework nevű mappába helyezd el.
#
#
import string
abc = list(string.ascii_lowercase[0:26])
print(abc)

ascii = []
for i in abc:
    ascii.append(ord(i))
print(ascii)

def pairing(ascii, abc):
    for num, chr in zip(ascii, abc):
        print(num, chr)

pairing(ascii, abc)

# még 10 soronként tördelni kell, de még erre sem találtam megoldást

#
# Kriszti
# def checkalpha(counter):
#     if chr(counter).isalpha():
#         return chr(counter)
#     else:
#         return ""
#
# def check_last_column(counter):
#     if chr(counter).isalpha():
#         return counter
#     else:
#         return ""
#
# counter = 97
# for i in range(10):
#     print(chr(counter), counter,
#           chr(counter + 10), counter+10,
#           checkalpha(counter + 20), check_last_column(counter + 20))
#     counter += 1

# print(chr(97))
# print(ord('a'))

# a_betu = abc[0]
# print(a_betu)
# ord(a_betu)
# print(ord(a_betu))

# betuk = []
# for i in abc:
#     betu = int(ord(abc[i]))
#     betuk.append(betu)
# print(betuk)

#
# ascii = []
# for i in abc:
#     convert = ord(abc[i])
#     ascii.append(convert)
# print(ascii)
# # ascii = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]

