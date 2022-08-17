#Factorial using Recursion

def factorial_rec(n):
    if (n==0):
        return 1
    return factorial_rec(n-1) * n

num = input('Enter value of n: ')
n = int(num)
print(factorial_rec(n))

