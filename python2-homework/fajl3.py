# 3.	Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát egy sorként egy
# másik fájlba!

with open('adat.txt', 'r') as f:
    # sorok = f.readlines() # listaként kiírva
    sorok = f.read().replace('\n', ' ') # egy sorként kiírva

with open('adat_fajl3.txt', "w") as uj:
    uj.write(str(sorok))
    uj.close()
