import math
n = int(input()) #input number of elements in a list
sum = 0
ele_list = []

ele_list = list(map(int, input().split())) # input elements of list
freq = list(map(int,input().split()))
s = []

def median(ele):
    #computing MEDIAN
    n = len(ele)
    if n % 2 == 0:
        ele.sort()
        median = (ele[int((n / 2) - 1)] + ele[int((n / 2) + 1) - 1]) / 2
        return int(median)
    else:
        ele.sort()
        median = ele[math.floor(int(n / 2))]
        return int(median)

def quartiles():
    ele_list.sort()
    med = median(ele_list)
    q1 = []
    q2 = med
    q3 = []
    flag = False
    for i in ele_list:
        if i < med :
            q1.append(i)
        elif i == med:
            if flag:
                q3.append(i)
                flag = True
        elif i > med:
            q3.append(i)

    print (median(q1))
    print (q2)
    print (median(q3))

def create_dataset():
    for i in range(len(ele_list)):
        for j in range(freq[i]):
            s.append(ele_list[i])

def interquartile_range():
    create_dataset()
    s.sort()
    l = len(s)
    if l % 2 == 0:
        q1 = s[0:int(l/2)]
        q3 = s[int(l/2):l]
    else:
        q1 = s[0:math.floor(int(l / 2))-1]
        q3 = s[math.floor(int(l / 2))+1:l]

    interquartile_range = median(q3) - median(q1)
    print (round(float(interquartile_range),1))

quartiles()
interquartile_range()

