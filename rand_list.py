# liste mit zufälligen Zahlenwerten (Skript Seite 89)

# Schreiben sie ein Programm, das in einer Liste verschiednee zufällige Zahlenwerte 
# speichert und anschließend aus allen Werten der Liste den Mittelwert berechnet.

# Ergänzung 1: Erweitern sie eine eigene Funktion zur Mittelwertberechnung der Liste:
import random

def createRandomList(lengList, a, b) -> list:
    liste = []
    for i in range(lengList):
        liste.append(random.randint(a,b))
    return liste

def mittelwert(a, list) -> int:
    return sum(list) / a

def difNachbar(list) -> int:
    for i in range(len(list)- 1):
        print(abs(list[i] - list[i+1]))

def main():
    hauptliste = createRandomList(3, 10, 40)
    print(hauptliste)
    print(mittelwert(len(hauptliste), hauptliste))
    difNachbar(hauptliste)

if (__name__ == "__main__"):
    main()