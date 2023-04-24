#!python3

"""
Population growth can be modeled with the equation P = p*(1+r)^n
Where 
P is the future Population
p is the current population
r is the annual rate of grown as a decimal
n is the number of years

Write a function to determine the future population

Given 2 groups with given starting populations and different rates of growth,
determine how many years in the future they will have the same population or 
if they are diverging and will never have the same population
"""
import math

def population(p,r,n):
    return (p*((1+r)**n))


def equal(p1,r1,p2,r2):
   r1 = 1+r1
   r2 = 1+r2
   if r1==r2:
       return None
   elif (p1==0 and p2>0) and 0>r2:
       return math.log((p1/p2), (r2/r1))
   elif (p2==0 and p1>0) and 0>r1:
       return math.log((p2/p1), (r1/r2))
   elif math.log((p2/p1), (r1/r2))>=0:
       return math.log((p2/p1), (r1/r2))
   else:
       return None



def tests():
    assert round(population(1000,.05, 5)) == 1276
    assert round(population(1000,.02, 20)) == 1486
    assert equal(1000,.05,2000,.06) == None
    assert round(equal(1000,.03,2000,.01)) == 35    

tests()