import math

X = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
Y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

xy_mul = 0
x_sum = 0
y_sum = 0
x_sq_sum = 0
y_sq_sum = 0
n = 10

for i in range(10):
    xy_mul = xy_mul + X[i] * Y[i]
    x_sum = x_sum + X[i]
    y_sum = y_sum + Y[i]
    x_sq_sum = x_sq_sum + X[i] * X[i]
    y_sq_sum = y_sq_sum + Y[i] * Y[i]

correlation = (n * (xy_mul) - x_sum * y_sum) / math.sqrt(
    (n * x_sq_sum - (x_sum * x_sum)) * (n * y_sq_sum - (y_sum * y_sum)))

print(correlation)