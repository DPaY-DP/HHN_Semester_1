"""
Einführung in die Programmierung
Dateien öffnen und schließen, schreiben und lesen

Vor dem Lese- oder Schreibzugriff muss Datei zunächst geöffnet werden, dazu
stehen verschiedene Modi zur Verfügung

Standardmodus: r - Lesender Zugriff, Datei muss existieren

Schreibmodus: w  - Schreibender Zugriff, Datei wird neu angelegt, wenn sie nicht
existiert, eventuell bestehende Datei gleichen Namens wird überschrieben
"""

# Datei zum Schreiben öffnen: datei = open("Pfad zur Datei", "w")


# In Datei schreiben: datei.write(s)


# Schließen der Datei nach Abschluss der Schreiboperationen: datei.close()



# Datei zum Lesen öffnen: datei = open("Pfad zur Datei", "r")


# Funktionen zum Lesen aus einer Datei: datei.read(x), datei.readlines()


# Schließen der Datei nach Abschluss der Leseoperationen: datei.close()
