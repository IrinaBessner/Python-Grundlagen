
#GAnzzahlen (int)
age: int=25  
print(age)

#Fließkommazahlen (float)
pi:float=3.14159 
print(pi)


#Fließkommazahlen (float)
is_active: bool=True
print(is_active)

name: str="Irina"
print(name)

#Listen (list) - veränderbar
fruits: list[str]=["Apfel","Banane", "Kirsche"]
fruits.append("Orange")
print(fruits)

#Tupel (tuple) - unveränderbar
coordinates: tuple[float, float]=(52.5,13.4)
print(coordinates)

#ListMengen (set) - keine Duplikate, Reienfolge egal
uniquqe_numbers: set[int]={1,2,3,3,2}
print(uniquqe_numbers)


#Dictionaries (dict) - Schlüssel/Wert-Paare
person:dict[str, str | int]={
    "name": "Eva",
    "age": 7
}
print(person["name"])  
print(person["age"])
print(person)


#NoneType - spezielle "kein Wert" - variable
result: None=None
print(result)

