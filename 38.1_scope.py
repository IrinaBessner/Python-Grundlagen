def my_function():
    print("In my function.")

    def my_nested_function():
        print("In my nested function.")
        print("Exiting my nested function.")

    print("About to call the nested function.")
    my_nested_function()

my_function()
# my_nested_function() ← würde hier einen Fehler geben
