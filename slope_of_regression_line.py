
#using python libraries

# from statistics import mean
# import numpy as np
#
# x = np.array([15, 12, 8, 8, 7, 7, 7, 6, 5, 3], dtype=np.float64)
# y = np.array([10, 25, 17, 11, 13, 17, 20, 13, 9, 15], dtype=np.float64)
#
# def regression_line_slope(x,y):
#     slope = (((mean(x)*mean(y)) - mean(x*y)) /
#          ((mean(x)**2) - mean(x**2)))
#     return slope
#
# slope = regression_line_slope(x,y)
# print(round(slope, 3))
#



# without using any libraries


x = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

def mean(ele):
    sum = 0
    for i in ele:
        sum = sum + i
    return sum / len(ele)

def regression_line_slope(x,y):
    xy = []
    x_sq = []
    for i in range(10):
        xy.append(x[i]*y[i])
        x_sq.append(x[i]**2)
    slope = (((mean(x)*mean(y)) - mean(xy)) /
         ((mean(x)**2) - mean(x_sq)))
    return slope

slope = regression_line_slope(x,y)
print(round(slope, 3))