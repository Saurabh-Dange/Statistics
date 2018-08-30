import math
n = int(input()) #input number of elements in a list

ele_list = []

ele_list = list(map(int, input().split())) # input elements of list

def mean(ele):
    sum = 0
    #computing MEAN
    for i in ele:
        sum = sum + i
    return sum / n

def standard_deviation(ele,mean):
    sq_mean_dist = 0
    for i in ele:
        sq_mean_dist = sq_mean_dist + (i - mean)**2
    print(round(math.sqrt(sq_mean_dist / len(ele)),1))

m = mean(ele_list)
standard_deviation(ele_list,m)
