def my_function():
    local_var = "Ich existiere nur hier drin"
    print (local_var)

my_function() 
# print(local_var)

x="ich existiere global/überall"
print(x)

def my_func():
    global x
    x = "ich existiere jetzt überall"
    print(x)

my_func()
def my_func1():
    global x
    x = "ich existiere hier"
    print(x)
my_func1()