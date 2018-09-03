import math

p = 0.12  # probability of child being boy
q = 0.88  # probability of child being girl

n = 10  # total number of child in family
x = 2
value1 = 0
value2 = 0


def ncr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)


for i in range(3): # for atmost two
    value1 = value1 + ncr(n, i) * (p ** i) * (q ** (n - i))

for i in range(2, n + 1): #for atleast two
    value2 = value2 + ncr(n, i) * (p ** i) * (q ** (n - i))

print(round(value1, 3))
print(round(value2, 3))