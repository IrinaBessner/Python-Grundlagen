#a=10
#b=9
#if a > b :
 #   print("a gröser als b")

 #   my_var=True
 #Irina   print(my_var)


print("Enter your name:")
player_name = input().strip()

print("Is the player already started? Enter 'y' for yes and 'n' for no.")
player_starter = input().strip().lower()

print("The player answer is:")
print(player_name)

if player_starter == "y":
    print("(starter)")
elif player_starter == "n":
    print("(not started)")
else:
    print("Bitte nur 'y' oder 'n' eingeben.")