x=10  # global

def my_func():
    x=10
    print("In my_func, x ="+ str(x))  # → 10

    def my_nested_func():
        nonlocal x
        x=100
        print("In my_nested_func, x = "+ str(x)) #→ 100

    my_nested_func()  
    print("At and of my_func, x = "+ str(x))#→ 100  

my_func()
print("Outside of functions, x = "+ str(x)) #→ 10




