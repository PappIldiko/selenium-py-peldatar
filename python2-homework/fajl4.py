# 4.	Olvasd be a fájlt, tárold a sorokat listában,
# majd írd ki a lista tartalmát így, ahogy beolvastad, soronként egy szóval egy másik fájlba!

with open('adat.txt', 'r') as f:
    sorok = f.readlines() # listaként kiírva

with open('adat_fajl4.txt', "w") as uj:
    for i in sorok:
        uj.write(i)
