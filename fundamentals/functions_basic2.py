#countdown

def  countDown(num):
    newList = []
    for i in range(num, -1, -1):
        newList.append(i)
    return newList
print(countDown(5))

#print and return

def print_return(list):
    print(list[0])
    return list[1]
print (print_return([1,2]))

#first plus length
def first_plus_length(list):
    print(list[0])
    return len(list)
print(first_plus_length([1,2,3,4,5]))

# value greater
def valueGreater(list):
    if len(list)<2:
        return False
    newList = []
    for val in list:
        if val>list[1]:
            newList.append(val)
    print(len(newList))    
    return newList
print(valueGreater([5,2,3,2,1,4]))
print(valueGreater([5,2,3,2,1,4]))
print(valueGreater([1]))
print(valueGreater([]))

#this length
def lengthValue(size,value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList
print(lengthValue(4,7))
