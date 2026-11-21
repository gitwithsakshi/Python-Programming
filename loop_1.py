numbers = [1,-1,2,-2,3,4,-5]

largest = numbers[0]

for x in numbers:
    if x>largest:
        largest=x
print(largest) #My mistake: I was print "x" instead of largest number..x is the current elements.