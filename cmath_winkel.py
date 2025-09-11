import cmath  #bibliothek für komplexe Mathematik

z=3+4j

#Betrag (länge) und Winkel (phase)
betrag= abs(z)
winkel= cmath.phase(z)

print("z= ", z)
print("Betrag", betrag)
print("Winkel (Radiant)", winkel)

