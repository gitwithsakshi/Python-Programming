#Calculate the factorial of a number.

n=int(input("Enter:"))
factorial = 1
# Loop from 1 to n
for i in range(1, n + 1):
    factorial *= i
print(factorial)

#Using while loop
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1

print(fact)


