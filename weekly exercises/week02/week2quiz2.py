import math
# -*- coding: utf-8 -*-
# Created on Tue Oct 15 17:17:13 2024

# @author: hamilla1
def isprime(x):
    if x <= 1:
        return False
    for i in range (2, int(math.sqrt(x))+1):
        if x % i == 0: 
            return False
    return True

def primesInList(mylist):
    primelist = [] 
    for x in mylist:
        if isprime(x) == True:
            primelist.append(x)
    return primelist
                   

    
 	

mylist = list(range(1, 100))
primes = sorted(primesInList(mylist))
print(primes)




  


