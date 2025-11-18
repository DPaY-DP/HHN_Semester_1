import random

minzahl = 1
maxzahl = 100

print("Zahlenratespiel")

ratezahl = random.randint(minzahl, maxzahl)

zahl = None
while zahl != ratezahl:
    zahl = int(input(f"Bitte Zahl zwischen {minzahl} und :{maxzahl} raten: "))

    if zahl == ratezahl:
        print("Gewonnen! Zahl erraten.")
    elif ratezahl < zahl:
        print("Zu ratende Zahl ist kleiner")
    else:
        print("Zu ratende Zahl ist groesser")
