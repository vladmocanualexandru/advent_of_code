import math

def isPrime(number):
    if number>1:
        for d in range(2, int(math.sqrt(number))+1):
            if number % d == 0:
                return False
        else:
            return True
    else:
        return False

def splitIntoPrimeDivisors(number):
    divs = []

    for d in range(2, int(number/2)+1):
        while number%d==0 and isPrime(d):
            divs.append(d)
            number/=d

    return divs

def splitIntoPrimeDivisorsPow(number):
    divs = {}

    for primeDiv in splitIntoPrimeDivisors(number):
        if not primeDiv in divs:
            divs[primeDiv] = 1
        else:
            divs[primeDiv]+=1

    return divs