x = 1112 #global
x2 = 23
x3 =26

def my_function():
    x = 2222 #local
    print("in my_function, x = " + str(x)) #2222

    def my_nested_function():
        x = 3333 #local in my_nested_function
        print("in my_nested_function, x = " + str(x)) #3333
        print("my i nested function can access variables from the outer function")

    print("call my nested function")
    my_nested_function()

my_function()
print("in the global scope, x = " + str(x)) #1112
print("in the global scope, x2 = " + str(x2)) #23
print("in the global scope, x3 = " + str(x3)) #26