p = 1/3 # probability of fault detection
q = 2/3 # probability of success
n = 5 # no of independent events
value2 = 0
value = q

value = p + q*p + (q ** 2 )*p +(q ** 3 )*p + (q ** 4 )*p  # probability of fault detection before or at 5th  round

print (round(value,3))