import math
mean = 2.5
x = 5

poisson_distribution = ((mean ** x) * math.exp(-mean))/math.factorial(x)

print (round(poisson_distribution,3))