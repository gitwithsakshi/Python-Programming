#Sum of even numbers upto given number n.

n = int(input("Enter your number "))
sum=0

for x in range(1, n+1):
    if x % 2 == 0:
     sum+=x

print(sum)
