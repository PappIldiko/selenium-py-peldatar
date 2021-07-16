# 2.	Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát egy sorban!

with open('adat.txt', 'r') as f:
    sorok = f.readlines()
    print(sorok)

