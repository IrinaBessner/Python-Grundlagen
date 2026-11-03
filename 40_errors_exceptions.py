#Syntxfehler
value=int(input())
value==10
print (value)


zahl=5 
if  zahl>3:
    print("Zahl ist größer als 3")

#Laufzeitfehler    
zahlen = [10, 20, 30]
index = 5
print(zahlen[index])


#Logische Fehler
def durchschnitt(werte):
    summe = 0
    for wert in werte:
        summe += wert
    return summe / (len(werte) - 1)

noten = [2, 3, 1, 4]
print("Durchschnitt:", durchschnitt(noten))
    
