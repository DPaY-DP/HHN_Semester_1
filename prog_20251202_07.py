"""
Einführung in die Programmierung
Laufzeitfehler

Bei Auftreten eines Fehlers bricht Programm vorzeitig ab und gibt Fehlermeldung aus

Fehlermeldung enthält Stelle des Programms, an der der Fehler auftritt und Art des Fehlers:
"""

int(input("Bitte geben Sie eine Zahl ein: "))

"""
Bitte geben Sie eine Zahl ein: hallo
Traceback (most recent call last):
  File "......py", line 10, in <module>
    int(input("Bitte geben Sie eine Zahl ein: "))
ValueError: invalid literal for int() with base 10: 'hallo'
"""
