age= int(input("Wie alt bist du?"))

if age<12:
    print("Du bist ein Kind.")
elif age<18:
    print("Du bist ein Teenager.")
elif age<65:
    print("Du bist ein Erwachsener.")
else:
    print("Du bist im Renteralter.")

    temperature =30

    if temperature>30:
        print("Es ist sehr heiß.")
    elif temperature>20:
        print("Es ist warm")
    else:
        print("Es ist kühl oder kalt")

    x=5
    y=12

    #Erstes if-else
    if x>10:
        print("x iszt größe als 10")
    else:
        print("x ist NICHT größe als 10")

    age =20
    if age>= 18:
        print("Du bist volljährig.")
    else:
        print("Du bist minderjährig.")
    

#ELIF
my_number=int(input("Gib ein Zahl ein: "))
if my_number<0:
    print("Die zahl ist negativ.")
elif my_number==0:
    print("Di Zahl ist null.")
else :
    print("Die Zahl ist positive")
    print("Danke fürs Mitmachen")



password = "StrongPass123!"

length = len(password)

if length < 4:
    print("Passwort ist sehr schwach.")
elif length < 8:
    print("Passwort ist schwach.")
elif length < 12:
    print("Passwort ist mittel.")
elif length < 16:
    print("Passwort ist stark.")
else:
    print("Passwort ist sehr stark.")
