# #finally  wird immer ausgeführt, egal ob ein Fehler auftritt oder nicht.
# try:
#     zahl = 10 / 0

# except ZeroDivisionError:
#     print("Fehler: Division durch 0!")

# finally:
#     print("Das Programm ist beendet.")





# # raise  kannst du selbst einen Fehler auslösen.

# alter = -5

# if alter < 0:
#     raise ValueError("Das Alter darf nicht negativ sein!")

# print("Alter:", alter)




#Zusammen
try:
    alter = int(input("Wie alt bist du? "))

    if alter < 0:
        raise ValueError("Alter darf nicht negativ sein!")

except ValueError as e:
    print("Fehler:", e)

else:
    print("Dein Alter ist:", alter)

finally:
    print("Programm beendet.")

