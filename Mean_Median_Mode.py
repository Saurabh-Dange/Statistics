n = int(input()) #input number of elements in a list
sum = 0
ele = []

ele = list(map(int, input().split())) # input elements of list

def mean():
    #computing MEAN
    for i in ele:
        sum = sum + i
    print(sum / n)

def median():
    #computing MEDIAN
    if n % 2 == 0:
        ele.sort()
        median = (ele[int((n / 2) - 1)] + ele[int((n / 2) + 1) - 1]) / 2
        print(median)
    else:
        ele.sort()
        median = ele[int(n / 2)]
        print(median)

def mode():
    #computing MODE
    min_ele = ele[0]  # min_ele
    min_count = 1  # min_count

    for i in ele:
        count = ele.count(i)
        if count > min_count:
            min_count = count
            min_ele = i
        elif count == min_count:
            if i < min_ele:
                min_ele = i

    print(min_ele)

mean()
median()
mode()