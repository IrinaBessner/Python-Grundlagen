
#n Python sind Sammlungen Datenstrukturen, die mehrere Werte gleichzeitig speichern können: 
# Listen (veränderlich, mit Reihenfolge), 
# Tupel (unveränderlich), 
# Mengen (keine Reihenfolge, keine Wiederholungen), 
# Wörterbücher (Schlüssel-Wert-Paare).

#Liste 
zahlen=[1,2,3]     #Ich habe eine Liste mit den Zahlen [1, 2, 3] erstellt und sie der Variablen zahlen zugewiesen.
zahlen.append(4)   #Wir haben die Zahl 4 am Ende der Liste hinzugefügt.

print("Liste: ", zahlen)

#Tuple
koordinaten= (10,20)
#  koordinaten [0]=15 - Fehler!!!   Tuple ist unveränderbar
#  Ich initialisiere die Variable koordinaten und weise ihr das Tupel (10, 20) zu.
#  Ein Tupel ist eine unveränderbare Datenstruktur – das heißt, ihre Elemente können nach der Initialisierung nicht verändert werden.

#Set (Menge)
farben={"rot", "blau", "grün"}
farben.add("gelb")            # Mit der Methode add füge ich ein Element in einen Set hinzu.    farben={"rot", "blau", "grün", "gelb"}
#  ich deklariere und initialisiere  die Variable farben, indem ich ihr die Menge 
#  mit den Werten "rot", "blau" und "grün" zuweisen.
#  Ich füge der Menge farben das neue Element "gelb" hinzu.

# Dictionary
student ={ "name": "Lina"}
#   Ich deklariere die Variable student als Dictionary und initialisiere sie 
#   mit dem Schlüssel-Wert-Paar "name": "Lina".
#   Ich initialisiere das Dictionary student und weise ihm das Schlüssel-Wert-Paar
#   "name": "Lina" zu.
#   Das bedeutet: der Schlüssel "name" ist mit dem Wert "Lina" verknüpft.


