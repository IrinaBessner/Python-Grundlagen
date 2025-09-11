früchte=["Apfel","Banane","Kirsche","Dattel", "Erdbeere"]
print(früchte[0]) 

früchte.append("Orange") #fügt die Element hinzu
print(früchte)
print(len(früchte))

früchte.remove("Banane") #löscht 
print(len(früchte))
früchte.pop(1)
print(früchte) # zeigt die Zahl der Elemente n in der Liste

del früchte[-1] # entfernt die Element an der letzten Position 
print(früchte)
del früchte[0]
print(früchte)


element = früchte.pop(0)