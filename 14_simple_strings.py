#1.Simple Strings
text="Hallo Welt"
print(text )   #Ausgabe 

#2. String Quotes ( Einzel- und Doppel-Anführungszeichen)
a='Hallo'
b="Welt"
print(a,b)

#3. String mit Escaped Quotes
# Mit \ kann man Anführungszeichen entkommen (escaped)
text= "Er sagte: \"Hallo\""
print(text)

#4.Escape Sequences
#Besondere Zeichen wie \n (Neue Zeile) ode t (Tab)
text="Zeile 1\nZeile 2 \tmit Tab"
print(text)

#5. Raw StringsTriple Quoted Strings
#- Raw Strings ignorieren Escape-Sequenzen(r"..."")
#- Triple Quotes ''' oder """
raw= r"C:\Users\Name\Desktop"
print(raw)

multi="""Das ist
ein mehrzeiliger
String"""
print(multi)

#6. String Operations
#String kann man verbinden(+), wiederholen(*), Länge messen(len()), und Indizierung benutzen

a="Hallo"
b="Welt"
print(a+ " " + b)  # Konkatenation -> Hallo Welt
print(a*3)         # Wiederholung -> HalloHalloHallo
print(len(a))      # Länge -> 5
print(a[1])        # Index-> 'a'