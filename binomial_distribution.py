import math

boys = 0.52 #probability of child being boy
girls = 0.48 #probability of child being girl

n = 6 # total number of child in family
x = 3
value = 0


def ncr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)


for i in range(3,n+1):
    value = value + ncr(6, i) * (boys ** i) * (girls ** (n-i))
    


print(round(value,3))