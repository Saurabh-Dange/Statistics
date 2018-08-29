n = int(input()) #input number of elements in a list
ele = list(map(int, input().split())) # input elements of list
weight = list(map(int, input().split())) # input weight  of elements

wt_ele = 0 #sum of multiplication of weight and element
wt = 0 #sum of total weights

for i in range(n):
    wt_ele = wt_ele + weight[i]*ele[i]
    wt = wt + weight[i]

weighted_mean = float(wt_ele/wt)

print (round(weighted_mean, 1))