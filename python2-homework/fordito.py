# Írj egy Python programot, amely a felhasználótól pozitív számokat kér be mindaddig, amíg a felhasználó nullát nem ad be! A program az összes értéket tárolja egy listában, majd írja ki a képernyőre a lista elemeit fordított sorrendben!

flag = True
lista = []

while flag:
    try:
        num = input("Enter a positive number:")
        if int(num) > 0:
            lista.append(int(num))
        elif int(num) < 0:
            print("This isn't a positive number.")
        else:
            flag = False

    except ValueError:
        print("This isn't an integer.")


lista.reverse()
print(f"The reversed list of your numbers is {lista}")


