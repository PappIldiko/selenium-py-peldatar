# Az autód 7 litert fogyaszt országúton és 9-et városban. A hévízi üdülésedre 170 kilómétert utazol országúton és 35-öt városban. Mennyit fogyaszt az autód csak oda? És oda-vissza? Mennyibe kerül a teljes út, ha 350 Ft a benzin? Oldd meg ezt feladatot úgy, hogy nem előre megadott értékekkel (országúti fogyasztás, városi fogyasztás, országúton megtett út, városban megtett út, benzin ára) dolgozol, hanem a felhasználótól kéred ezeket be. Ahol szükséges, ne feledd konvertálni az értékeket!
# A megoldást egy consumption.py nevű file-ban kell beadnod.

# felhasználótól bekért értékekkel

road_consumption = int(input("Adja meg az országúti átlagfogyasztását l-ben: "))  # l/km
city_consumption = int(input("Adja meg a városi átlagfogyasztását l-ben: "))  # l/km

road_trip = int(input("Adja meg az országúton megtett út hosszát km-ben: "))  # km
city_trip = int(input("Adja meg az városban megtett út hosszát km-ben: "))  # km

price_of_gas = int(input("Adja meg a benzin árát Ft-ban: "))  # Ft

print("*" * 30)
consumption_one_way = road_consumption / 100 * road_trip + city_consumption / 100 * city_trip
print("Fogyasztás egy útra: " + str(consumption_one_way) + " l.")
consumption_turnaround = consumption_one_way * 2
print("Fogyasztás a teljes útra: " + str(consumption_turnaround)  + " l.")
price_of_trip = consumption_turnaround * price_of_gas
print("A teljes út ára: " + str(price_of_trip) + " Ft.")


# fix értékekkel

road_consumption = 7  # l/km
city_consumption = 9  # l/km

road_trip = 170  # km
city_trip = 35  # km

price_of_gas = 350  # Ft

print("*" * 30)
consumption_one_way = road_consumption / 100 * road_trip + city_consumption / 100 * city_trip
print(consumption_one_way)
consumption_turnaround = consumption_one_way * 2
print(consumption_turnaround)
price_of_trip = consumption_turnaround * price_of_gas
print(price_of_trip)
