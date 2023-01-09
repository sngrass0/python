# this is a single line comment
"""
This is
a multiline
comment
"""
my_new_favorite_language = 'Python' # variable declaration, initialize string

# [lines 10 - 16] variable declaration
num1 = 42 # primitive, numbers
num2 = 2.3 # primitve, numbers (float)
boolean = True # primitive, boolean
string = 'Hello World' # primitive, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # composite, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # composite, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # composite, initialize tuple

print(type(fruit)) # log statement
print(pizza_toppings[1]) # log statement
pizza_toppings.append('Mushrooms') # add value to list
print(person['name']) # log statement, access value of dictionary
person['name'] = 'George' # change value in dictionary
person['eye_color'] = 'blue' # add new value field to dictionary
print(fruit[2]) # log statement, access value in tuple

if num1 > 45: # if statement 
    print("It's greater") # log statement
else: # else statement
    print("It's lower") # log statement

if len(string) < 5: # if statement, length check
    print("It's a short word!") # log statement
elif len(string) > 15: # else if statement, length check
    print("It's a long word!") # log statement
else: # else statement
    print("Just right!") # log statement

for x in range(5): # for loop, start: 0 stop: 4
    print(x) # log statement
for x in range(2,5): # for loop, start: 2 stop: 4
    print(x) # log statement
for x in range(2,10,3): # for loop, start: 2 stop: 9 increment: +3
    print(x) # log statement
x = 0 # variable declaration
while(x < 5): # while loop, start: 0 stop: >5
    print(x) # log statement
    x += 1 # increment: +1

pizza_toppings.pop() # delete last value from list
pizza_toppings.pop(1) # delete value at index 1 from list

print(person) # log statement
person.pop('eye_color') # delete value from dictionary
print(person) # log statement

for topping in pizza_toppings: # for loop, sequence: pizza_toppings
    if topping == 'Pepperoni': # if statement
        continue # continue back to top of loop
    print('After 1st if statement') # log statement
    if topping == 'Olives': # if statement
        break # break out from for loop

def print_hello_ten_times(): # function header
    for num in range(10): # for loop, start: 0 stop: 9
        print('Hello') # log statement

print_hello_ten_times() # function call

def print_hello_x_times(x): # function, parameter: x
    for num in range(x): # for loop, start: 0 stop: x - 1
        print('Hello') # log statement

print_hello_x_times(4) # function call, passing argument: 4

def print_hello_x_or_ten_times(x = 10): # function, parameters: x = 10
    for num in range(x): # for loop, start: 0 stop: x - 1 or 9
        print('Hello') # log statement

print_hello_x_or_ten_times() # function call, arguments: none
print_hello_x_or_ten_times(4) # function call, arguments: 4


"""
Bonus section
"""

# print(num3)  # NameError: name <variable name> is not defined
# num3 = 72
# fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError: 'favorite_team'
# print(pizza_toppings[7]) # IndexError: list index out of range
#   print(boolean) # IndentationError: unexpected indent
# fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) #AttributeError: 'tuple' object has no attribute 'pop'