def factorial(limit):
    factorial = 1
 
    for i in range(1, limit + 1):
        factorial = factorial * i
 
    return factorial
 
#Print factorial from 1 to 10
for i in range(1, 10):
    print(factorial(i))