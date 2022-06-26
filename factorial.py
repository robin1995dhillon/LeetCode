def factorial(n):
    if(n==1):
        return n
    else:
        return n*factorial(n-1)


val = factorial(5)
print(val)