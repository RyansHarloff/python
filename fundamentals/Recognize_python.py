num1 = 42 # variable 
num2 = 2.3 # variable
boolean = True # data type
string = 'Hello World' # string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #tuple
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary
fruit = ('blueberry', 'strawberry', 'banana')#list
print(type(fruit))#parameter
print(pizza_toppings[1])#tuple access value
pizza_toppings.append('Mushrooms')#tuple change value
print(person['name'])#function parameter
person['name'] = 'George'#dictionary access value
person['eye_color'] = 'blue'#dictionary add value
print(fruit[2])#list access value

"""if num1 > 45:
    print("It's greater")
else:
    print("It's lower")""" # conditional if/else

"""if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")""" # conditional else/if

"""for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1"""#conditional for loop/ while loop

pizza_toppings.pop()# tuple remove value end of array
pizza_toppings.pop(1)# tuple remove value at position 1

"""print(person)
person.pop('eye_color')
print(person)"""#function parameter, # remove eye color from dictionary

"""for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break"""#for loop #if statement

"""def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()"""#variable declartion for statement function parameter

"""def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)"""#variable declaration for statement 

"""def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)"""#variable declaration for statement print function parameter


"""
Bonus section
"""

# print(num3)# variable num is not defined
# num3 = 72 # index error out of range
# fruit[0] = 'cranberry'#tuple change value
# print(person['favorite_team'])# key error 
# print(pizza_toppings[7])#list index out of range
#   print(boolean) #unexpected indent
# fruit.append('raspberry')#tuple object has no attribute append
# fruit.pop(1)# tuple object has no attribute pop