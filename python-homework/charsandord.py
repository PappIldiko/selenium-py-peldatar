# Feladat: Python for ciklus gyakorlása
# A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható el a megoldás.
#
# rj programot, ami kiírja a kisbetűket, és melléjük az karakter kódjukat! A kiírás több oszlopos legyen, és legfeljebb 10 soros. Minta:
# a 97 f 102 .....
# b 98 g 103
# c 99 h 104
# d 100 i 105
# e 101 j 106
# A megoldashoz használd a beépített ord() es chr() függvényeket.
#
# A megoldást egy charsandord.py nevű file-ban kell beadnod.
#
# Feladat beadása
# A fent eméített python file-okat és benne a megoldásodat kérlek a saját selenium-py-peldatar github repo forkodban egy python-homework nevű mappába helyezd el.



import string
abc = list(string.ascii_lowercase[0:26])
ascii = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
# print(ascii)
# print(abc)

def pairing(ascii, abc):
    for num, chr in zip(ascii, abc):
        print(num, chr)

pairing(ascii, abc)

# még 10 soronként tördelni kell, de erre nem találtam megoldást

#
# import string
#
# raw = ''
#
# for i in range(0, len(string.ascii_lowercase)):
#     abc = string.ascii_lowercase[i]
#     if i > 0 and (i % 3) == 0:
#         print(raw + '')
#         raw = ''
#     raw += '\t' + abc + ' ' + str(ord(abc))
#     print(abc + '')



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

