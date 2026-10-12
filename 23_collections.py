empty_set = set()
print(empty_set)

string_set = {"apple", "banana", "cherry"}
print(string_set)

number_set = {1, 2, 3, 4, 5}
print(number_set)

mixed_set = {1, "apple", 3.14, True}
print(mixed_set)

# set methods
# add(element)
# remove(element)
# clear()

players = {"Alice", "Bob", "charlie"}
print(players)

players.add("David")
print(players)

players.remove("Bob")
print(players)

frozenset_example=frozenset({1,90.6, "Frozenset"})
print(frozenset_example)

#frozenset_example.add(2)  # This will raise an AttributeError since frozensets are immutable

#list erlaubt dublicate und die elemente konnen geaendert werden 
# und in der bestimmten Reihenfolge gespeichert werden
# und die elemente konnen in die bestimmten platz hinzugefügt werden

#[] - square brackets
#() - round brackets
#{} - curly brackets

#methods in python lists 

#@append(element) - adds an element to the end of the list
#@insert(index, element) - adds an element at a specific index
#@remove(element) - removes the first occurrence of an element
#clear() - removes all elements from the list
#count(element) - returns the number of occurrences of an element

my_list=[1,2.8, "Bob, 6+1j, True"]
print(my_list)

my_list.append("new element")
print(my_list)

my_list.append("new element")
print(my_list)

my_list.insert(0, "inserted element")
print(my_list)

my_list.remove(2.8)
print(my_list)

#Tuples
my_tuple=(7, 4.5-32,3j,-999.2, "what a great tuple, True")
print(my_tuple)

#Dictionary

my_dict={"name":"Alice","age":56, "city":"Honnover"}
print(my_dict)

my_dict.get("name") 
my_dict["age"]=57

print(my_dict.get("age"))

print(my_dict.get("name"))

print(my_dict.get("city"))