"""
Einführung in die Programmierung
Debugging: Finden logischer Fehler

Debugger ermöglichen einen Schritt-für-Schritt-Ablauf eines Programms, um sich
so z.B. die Inhalte von Variablen während des Programmablaufs ansehen zu können

Die folgende Funktion zur Ausgabe von Listen hat mehrere logische Fehler. Welche?
"""

def printlist(printlist):
    """Gibt alle Elemente einer Liste aus

    """
    liste = [printlist]
    for i in range(len(liste)):
        print(i)

data = [1,2,3,4,5]
printlist(data)
