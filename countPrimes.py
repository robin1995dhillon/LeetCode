import math


def countPrimes(n):
    if(n<2):
        return 0
    isPrime = [True] * n
    isPrime[0] = isPrime[1] = False

    for i in range (2,int(math.ceil(math.sqrt(n)))):
        if (isPrime[i]):
            for multiples_i in range(i*i,n,i): #if we put range(i,n,i), it will be wrong as for 2, even if it is prime, it will give ans as not prime
                isPrime[multiples_i] = False
    return sum(isPrime)
