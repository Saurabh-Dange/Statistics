import math
mean = 20
sd = 2

nd1 = 0.5 * (1 + math.erf((19.5 - mean)/(sd*math.sqrt(2))))
nd2 = 0.5 * (1 + math.erf((20 - mean)/(sd*math.sqrt(2))))
nd3 = 0.5 * (1 + math.erf((22 - mean)/(sd*math.sqrt(2))))

print(round(nd1,3))
print(round(nd3 - nd2,3))