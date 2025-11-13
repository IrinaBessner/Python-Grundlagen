print(5==5)   #True
print(5!=4)   #True
print(7>3)    #True
print(2>=2)   #True
print(1<9)    #True
print(3<=3)   #True

#Boolean Variablen
is_adult=True
is_student= False

print(is_adult)
print(type(is_student))


age= int(input("Wie alt bist du?"))
if age>=18: 
    print("Du bist volljahrig.")

number= int(input("<Gib eine Zahl ein: "))    
if number >100:
    print("Die Zahl ist größer als 100")


password=input("Passwort eingeben: ")

if password=="1234":
    print("Login erfolgreich.")