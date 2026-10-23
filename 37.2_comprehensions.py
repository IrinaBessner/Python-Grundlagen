"""my_numbers=[4,15,8,16,23,42]
my_new_numbers =[]
for x in my_numbers:
    my_new_numbers.append(x*x)
print(my_new_numbers)"""

my_numbers=[4,15,8,16,23,42]
my_new_numbers=[n*n for n in my_numbers]

print(my_new_numbers)

