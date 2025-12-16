woerterbuch = {"Tag": "day"}

while True:
    deutsch = input("Bitte deutsches Wort eingeben, Ende mit 0: ")

    if deutsch == "0":
        break
    
    if deutsch in woerterbuch:
        print(f"Englische Übersetzung: {woerterbuch.get(deutsch)}")
    else:
        print("Übersetzung nicht bekannt")
        englisch = input("Bitte englische Übersetzung eingeben: ")
        woerterbuch[deutsch] = englisch


