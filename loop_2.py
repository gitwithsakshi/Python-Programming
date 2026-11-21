numbers=[5,21,-5,-21,-1,1,0 ,0]

positive=0
negative=0
zero=0

for x in numbers:
    if x>0:
        positive+=1
    elif x<0:
       negative+=1
    else:
       zero+=1

print(positive)
print(negative)
print(zero)