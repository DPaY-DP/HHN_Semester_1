"""
Einführung in die Programmung
Dataeien öffnen und schließen, schreiben und lesen

Vor dem Lese- oder Schreibzugriff muss Datei zunächst geöffnet werden, dazu
stehen verschiedene Modi zur Verfügung

Standardmodus: r - lesender Zugriff, Datei muss existieren

Schreibmodus: w - Schreibender zugriff, Datei wird neu angelegt, wnn sie nicht
existiert, eventuell bestehedne Datei gleichen Namens wird überschrieben
"""

# Datei zum Schreiben öffnen: datei 0 open("Pfad zur Datei", "w")
datei = open("test.txt", "w")

# in Datei schreiben: datei.write(s)
datei.write("Das ist mein Text für meine Datei.\n")
datei.write("Noch mehr Text.")

#Schließen der Datei nach Abschluss der Schreiboperationen: datei.close()
datei.close()

#Datei zum Lesen öffnen: datei = open("Pfad zur Datei", "r")
datei = open("test.txt", "r")

# Funktionen zum Lesen aus einer Datei: datei.read(x), datei.readlines()
dateiinhalt = datei.readlines()

# Schließen der Datei nach Abschluss der leseoperationen: datei.close()
datei.close()

print(dateiinhalt)


