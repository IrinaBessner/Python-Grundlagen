# print("enter a number:")
# my_number=input()
# if int(my_number)<10:
#     print("Deine Number kleiner als 10")
#     print(my_number)    
# elif my_number ==10:
#         print("Deine Number ist gleich 10")
# else:
#     print("Deine Number größer als 10 ")
#     print(my_number)
# print ("Abgenmacht!")

# #Beispiel 2
# #punktzahl = 82
#print("enter deine Punktzahl:")
#punktzahl=input()

punktzahl=int(input("enter a number:"))

if punktzahl >= 95:
    print("Note: 1 - Ausgezeichnet")
elif punktzahl >= 85:
    print("Note: 2 - Sehr gut")
elif punktzahl >= 75:
    print("Note: 3 - Gut")        # ← das wird ausgegeben
elif punktzahl >= 60:
    print("Note: 4 - Befriedigend")
elif punktzahl >= 50:
    print("Note: 5 - Ausreichend")
else:
    print("Note: 6 - Nicht bestanden")
