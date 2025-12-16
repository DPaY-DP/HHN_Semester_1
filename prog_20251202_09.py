"""
Einführung in die Programmierung
Beispiel: CSV-Dateien schreiben
"""

# Adressliste
# jedes Element der Liste enthält Liste mit Adressdaten
liste = [["Max Müller", "Bahnhofstr. 12", "Heilbronn"],
         ["Susi Sorglos", "Hauptstr. 8", "Berlin"]]

# Liste soll als CSV-Datei mit folgendem Format gespeichert werden:
# Max Müller;Bahnhofstr. 12;Heilbronn
# Susi Sorglos;Hauptstr. 8;Berlin
adressstring = ""
for i in liste:
    for j in range(len(i)):
        adressstring += i[j] + ";"
    adressstring += "\n"
print(adressstring)

