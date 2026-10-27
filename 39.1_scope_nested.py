x = 10  # global

def meine_funktion():
    print(x)  # ✓ lesen funktioniert einfach so

meine_funktion()  # → 10

#Schreiben — dafür brauchst Du global:
x = 10  # global

def meine_funktion():
    global x       # ← sagt Python: ich meine die globale x
    x = 99         # ändert die globale Variable

meine_funktion()
print(x)  # → 99