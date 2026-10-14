
#print ("Input smth:")
#my_str=input()

#print("You entered :" ,my_str)

#my_string = input

#my_int = input()

while True:
    eingabe = input("Bitte eine Zahl eingeben: ")
    if eingabe.isdigit():
        zahl = int(eingabe)
        break
    print("Das ist keine gültige Zahl. Versuch es nochmal.")

print("Du hast eingegeben:", zahl)