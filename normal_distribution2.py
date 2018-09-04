import math
mean = 70
sd = 10

nd1 = 0.5 * (1 + math.erf((80 - mean)/(sd*math.sqrt(2))))
nd2 = 0.5 * (1 + math.erf((0 - mean)/(sd*math.sqrt(2))))
nd3 = 0.5 * (1 + math.erf((60 - mean)/(sd*math.sqrt(2))))

print(round((1-nd1)*100,2))
print(round((1-(nd3 - nd2))*100,2))
print(round((nd3 - nd2)*100,2))