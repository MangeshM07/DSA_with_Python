"""Asymptotic Analysis: (Theorotical Analysis)
    -> No dependency on machine, programming language, etc
    -> We do not have to implement all ideas and algorithms
    -> Asymptotic analysis is all about measuring order of growth in terms of size"""


# Order of growth - c2n+c3
def sumn(n):
    result=0
    for i in range(1,n+1):
        result = result+i
    return result

# Order of growth - c1
def sumf(n):
    return n*(n+1)/2

print(sumf(700000000000))
print(sumn(700000000000))


