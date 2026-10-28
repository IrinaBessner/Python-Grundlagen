def greet(name):
    print ("Hello, " +name) #name=Parameter

greet("Alina") # "Alina" =Argument

#Mehrere Argumente
def add(a,b):
    print(a+b)

add(3,7)    

#Default arguments
def do_math(a, b=1,c=2,d=3):
    result=a+b+c+d
    print("Sum ist: " +str(result))

do_math(1)
do_math(1,5)  
do_math(1,5,15)  

#Return value

def return_twothings(a,b):
    result1=a+b
    result2=a-b
    return result1,result2
print(return_twothings(5,6))  #(11, -1)

# verschiedene Datentypen
def person_info(name, phone, address, age):
    print(name)
    print("Phone: " +phone)
    print ("Address: " + address)
    print("Age: " + str(age))

person_info("Alyssa", "423-56", "196 Wandsbeck", 35)
person_info(age=32, name="Ruth", address="123 Berlin", phone="12345")
