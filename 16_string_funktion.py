# String-Formatierung mit .format()
# Mit Platzhaltern {} können Werte an beliebiger Stelle in einen String eingefügt werden.
text = "Hallo {}, willkommen in {}, heute ist {} .".format("Anna", "Berlin", "02.10.2025")
print(text)

# Die Reihenfolge der Platzhalter kann durch Indexzahlen gesteuert werden.
# {1} bedeutet: Nimm das zweite Argument, {0} das erste, {2} das dritte.
text = "Hallo {1}, willkommen in {0}, heute ist {2} .".format("Anna", "Berlin", "02.10.2025")
print(text)

# String-Slicing (Ausschnitt aus einem String)
# Teil 1: Einzelne Zeichen auslesen
my_string = "Hello World"
print(my_string)
print(my_string[0])      # erstes Zeichen
print(my_string[-2])     # zweites Zeichen von hinten

# Teil 2: Teilstrings mit Slice-Notation
# [start:stop] liefert Zeichen von Index start bis stop-1.
print(my_string[0:5])    # "Hello"
print(my_string[6:])     # ab dem Leerzeichen bis zum Ende
print(my_string[:5])     # erster Teil bis Index 4

print("------")

# Teil 3: Slices mit Schrittweite
# [start:stop:step] bedeutet: von start bis stop, aber nur jedes step-te Zeichen.
print(my_string[::2])    # jedes zweite Zeichen
print(my_string[::-1])   # String umkehren
print(my_string[1:5:2])  # Zeichen mit Schritt 2 im Bereich 1 bis 4
print(my_string[::2])    # gleiche Ausgabe wie oben

print(my_string[::1])    # gesamte Zeichenkette unverändert
print(my_string[:1])     # nur erstes Zeichen

print("========")

print(my_string[0::])   # gleicher Effekt wie gesamte Zeichenkette

print("--///////")

# .join() verbindet Listenelemente zu einem String.
# Das Zeichen vor .join() wird zwischen den Elementen eingefügt.
teile = ["Hallo", "Welt", "Python"]
text = ".".join(teile)
print(text)            # Hallo.Welt.Python
text = " ".join(teile)
print(text)            # Hallo Welt Python

print("SPLIT")
# .split() teilt einen String in eine Liste auf.
# Standardmäßig trennt es bei Leerzeichen.
text = "Apfel Banane Orange"
liste = text.split()
print(liste)           # ['Apfel', 'Banane', 'Orange']

# Wenn ein Trennzeichen angegeben wird, wird genau dort getrennt.
text2 = "eins zwei drei"
liste2 = text2.split(" ")
print(liste2)          # ['eins', 'zwei', 'drei']

# .upper() macht alle Buchstaben groß.
text = "hello world"
print(text.upper())    # HELLO WORLD

# .lower() macht alle Buchstaben klein.
text = "HELLO WORLD"
print(text.lower())    # hello world

# .replace() ersetzt einen Teilstring durch einen anderen.
text = "Python ist toll"
print(text.replace("toll", "super"))  # Python ist super

# .replace() kann auch mehrere Vorkommen ersetzen.
text = "Apfel, Apfel, Apfel"
print(text.replace("Apfel", "Birne"))  # Birne, Birne, Birne

