def dezimal_zu_binaer():
    zahl = int(input("Gib eine Dezimalzahl ein: "))
    binaer = bin(zahl)[2:]
    print(f"Die Binärdarstellung von {zahl} ist: {binaer}")

def binaer_zu_dezimal():
    binaer = input("Gib eine Binärzahl ein: ")
    dezimal = int(binaer, 2)
    print(f"Die Dezimaldarstellung von {binaer} ist: {dezimal}")

def menu():
    print("=== Binär-Konverter ===")
    print("1 – Dezimal → Binär")
    print("2 – Binär → Dezimal")
    auswahl = input("Wähle eine Option (1 oder 2): ")

    if auswahl == "1":
        dezimal_zu_binaer()
    elif auswahl == "2":
        binaer_zu_dezimal()
    else:
        print("Ungültige Eingabe")

menu()


