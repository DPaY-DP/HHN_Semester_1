anzahl = int(input("Bitte Anzahl eingeben: "))

for i in range(anzahl):
    for j in range(anzahl):
        if i == j or j == anzahl - 1 - i:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()