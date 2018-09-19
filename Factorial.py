number = int(input("Enter a number to calculate it's factorial: "))
factorial = 1
 
for i in range(1, number + 1):
    factorial = factorial * i
 
print("factorial of ", number, " is ", factorial)

