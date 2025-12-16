"""
Einführung in die Programmierung
Fehler abfangen

Fehler können durch try … except-Blöcke abgefangen werden

try leitet Ausnahmebehandlung ein, es werden alle Fehler innerhalb des
try-Blockes abgefangen
 
except-Zweig wird nur ausgeführt, wenn innerhalb des try-Blockes ein Fehler
aufgetreten ist

Je nach Art des Fehlers können verschiedene Ausnahmen (Exceptions) auftreten,
z.B. ValueError, TypeError, IOError, ZeroDivisionError
Liste der Ausnahmen in Python 3: https://docs.python.org/3/library/exceptions.html
 
Durch Definition mehrerer except-Blöcke kann eine genauere Fehlerbehandlung
erfolgen.

try … except-Blöcke können optional durch einen else- und einen finally-Zweig
erweitert werden.
"""

x = input("Bitte Zahl x eingeben: ")
y = input("Bitte Zahl y eingeben: ")

# Versuche Division x / y
try:
    erg = int(x) / int(y)
# Fehler bei Umwandlung in Integer-Zahl
except ValueError:
    print("Fehler: Keine Zahl")
# Fehler bei Division durch 0
except ZeroDivisionError:
    print("Fehler: Division durch Null!")
# Alle weiteren Fehler
except:
    print("Allgemeiner Fehler")
# Kein Fehler aufgetreten: Ausgabe Ergebnis
else:
    print("Das Ergebnis der Division ist %s." % erg)
# finally wird auf jeden Fall ausgeführt
finally:
    print("Programmende")
