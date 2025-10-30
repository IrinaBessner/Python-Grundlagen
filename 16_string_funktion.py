text= "Hallo {}, willkommen in {}, heute ist {} .".format("Anna", "Berlin", "02.10.2025")
print(text)
text= "Hallo {1}, willkommen in {0}, heute ist {2} .".format("Anna", "Berlin", "02.10.2025")
print(text)

#substring part 1
my_string= "Hello World"
print(my_string)
print(my_string[0])
print(my_string[-2])

#subsrting part 2
print(my_string[0:5])
print(my_string[6:])
print(my_string[:5])

print("------")

#substring part 3
print(my_string[::2])
print(my_string[::-1])
print(my_string[1:5:2])
print(my_string[::2])

print(my_string[::1])
print(my_string[:1])

print("========")

print(my_string[0::])

print("--///////" )

#.JOIN 

teile= ["Hallo", "Welt", "Python"]
text = ".".join(teile)
print(text)
text = " ".join(teile)
print(text)


print("SPLIT")
#.SPLIT
text= "Apfel Banane Orange"
liste=text.split()

print(liste)
text2="eins zwei drei"
liste2=text2.split(" ")
print(liste2)

#.UPPER

#.LOWER

#.REPLACE




