#basics
for i in range(151):
    print(i)

#Multiples of 5
for i in range(5,1001,5):
    print(i)

#counting the dojo way
for i in range(1, 100):
    if i % 5 == 0:
        print('Dojo')
    if i % 10 == 0:
        print('coding dojo')
    else:
        print(i)

#Woah thats a big number
maximum = int(500000)
total = 0

for number in range(1, maximum+1):
    if(number % 2 == 0):
        total = total + number

print("The Sum is {0} = {1}".format(number, total))

#countdown by fours
for i in range(2018,1,-4):
    print(i)

#flexible counter
lowNum = 2
highNum = 9
mult = 3

for x in range(2, 9, 3):
    if x % 3 == 0:
        print(x)
