from tkinter import N


def sum_rec(n):
    if n==0:
        return 0
    return sum_rec(n-1)+n
    
num=input('ENter Number: ')
n = int(num)
print(sum_rec(n))