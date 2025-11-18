liste = [100, 90, 30, 10, 11, 200]

# Ermitteln Sie die Anyahl der Elemente der liste:
print(len(liste))

# Geben Sie das dritte Element aus:
print(liste[2])

# Fügen Sie der liste das Element 300 hinzu:
liste.append(300)

# Sortieren Sie die Liste aufsteigend:
liste.sort()
print(liste)

# Geben Sie alle Elemente der Liste mit einer Schleife aus:
for i in range(len(liste)):
    print(liste[i])

for item in liste:
    print(item)

# Gegeben ist folgende mehrdimensionale Liste:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Geben sie das Element in der zweiten Zeile und ersten Spalte aus:
print(matrix[1][0])

# Aendern Sie das elment in der dritten Zeile und zweiten Spalte zu 10:
matrix[2][1] = 10
print()
# Berechnen Sie fuer jede Zeile der Liste matrix die Summe der Elemente:

for i in range(len(matrix)):
    print(sum(matrix[i]))