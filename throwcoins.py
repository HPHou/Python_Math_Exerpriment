import numpy as np 

NUM_EXER = 10000
count_max = 0

for i in range(NUM_EXER):
    L = []
    for i in range(100):
        if np.random.rand() > 0.5:
            L.append(1)
        else:
            L.append(0)

    C = []
    count = 1
    L.append(-1) #增加哨兵节点
    for i in range(len(L)-1):
        if L[i+1] == L[i]:
            count +=1
        else:
            if count>1:
                C.append(count)
            count = 1
    if np.max(C) >= 4:
        count_max +=1

print(count_max/NUM_EXER)