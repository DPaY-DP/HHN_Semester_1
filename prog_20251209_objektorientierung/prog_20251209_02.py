"""
Einführung in die Programmierung
Klassen und Objekte

Klasse: selbst definierter Datentyp, beschreibt Eigenschaften der Objekte,
        Bauplan für Objekte

Objekt: Exemplar oder Instanz einer Klasse

Eigenschaften einer Klasse:
    Attribute: Was hat das Objekt?
    Operationen: Was kann das Objekt?

Klassen definieren die Struktur und das Verhalten für eine Kollektion von
(gleichartigen) Objekten.

Objekte sind konkrete oder abstrakte Dinge dieser Welt. Sie besitzen einen
Zustand und reagieren mit einem definierten Verhalten:
    Der Zustand umfasst die Attribute sowie deren Werte.
    Das Verhalten wird durch die Methoden beschrieben.
"""

# Klasse Buch definieren:
class Buch:

    # Initialisierung von neunen Buch-Objekten
    def __init__(self, autor, titel, verlag, kennzeichen="ABC"):
        self.autor = autor
        self.titel = titel
        self.verlag = verlag
        self.kennzeichen = kennzeichen
        self.verfuegbar = True # jedes neue buch ist verfügbar

    # Umwandlung von Objekten in einen String (wird bei print-Ausgabe angewendet)
    def __str__(self):
        if self.verfuegbar:
            return f"{self.autor}: {self.titel} (Verlag: {self.verlag} ist verfügbar)"
        else:
            return f"{self.autor}: {self.titel} (Verlag: {self.verlag} ist ausgeliehen)"
        
    # Methoden zum Ausleihen, Zurückgeben und Abfragen des Status von Büchern
    def ausleihen(self):
        if self.verfuegbar:
            self.verfuegbar = False
            print("Buch wurde ausgeliehen.")
        else:
            print("Buch ist bereits ausgeliehen.")



# Objekte erzeugen und nutzen:
buch1 = Buch("Michael Kofler", "Python-Grundkurs", "Rheinwerk")
buch2 = Buch("Thomas Theis", "Einführung in Python", "Rheinwerk", "TTX")

print(buch1)
print(buch2)

buch1.ausleihen()

print(buch1)