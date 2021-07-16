# 5.	Olvasd be a fájlt, és írd ki a tartalmát egy másik fájlba, úgy, hogy nem tárolod el a szöveget,
# hanem minden sort azonnal kiírsz!

with open('adat.txt', 'r') as f:
    with open('adat_fajl5.txt', "w") as uj:
        for i in f.readlines():
            uj.write(i)

# másik opció
# with open("adat.txt", "r") as f, open("adat_fajl5.txt", "w") as uj:
#     uj.write(f.read())