# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:47:23 2023

@author: djlik
"""

import math
import numpy
import primesieve
import sympy
import time
from mpmath import *
mp.dps = 20; mp.pretty = True
start=time.time()

upper = 4.5*(10**8)
sumrecip = 0
mertenu=0.2614972128476427837554268386086958590517
mertenl=0.2614972128476427837554268386086958590516
flag=False
errornum=0
it = primesieve.Iterator()
print("Computing the sum of reciprocals of primes less than",upper)

for upperindex in range(math.ceil(upper/(10**8))):
    percent=str(round(upperindex/(upper/(10**10)), 2))
    sys.stdout.write('\033[2K\033[1G')
    print("Percent complete:",percent,end="\r")
    it.skipto(min(upper,(upperindex+1)*(10**8)))
    primemax = it.next_prime()
    primearray=primesieve.primes(upperindex*(10**8),primemax)
    noprimes=len(primearray)-1
    for index in range(noprimes):
        num=primearray[index]
        sumrecip = sumrecip + 1/num
        if (sumrecip-math.log(math.log(primearray[index+1]))-mertenu<0)or(sumrecip-math.log(math.log(num))-mertenl-2/(math.sqrt(num)*math.log(num))>0):
            flag=True
            errornum=num
    
print()
print("Sum of reciprocals of primes less than ",upper," is")    
print(sumrecip)
print("Exception found: ", flag,errornum)
print("Difference: ",sumrecip-math.log(math.log(num))-mertenu)
print("Total time taken:",time.time()-start,"seconds")