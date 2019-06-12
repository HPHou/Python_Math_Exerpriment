import numpy as np 
from numpy import random

NUM_STUDENT = 25
NUM_EXER = 10000

count=0

for i in range(NUM_EXER):
    birtdays = []
    for j in range(NUM_STUDENT):
        birtdays.append(np.random.randint(356))
    if len(set(birtdays)) < NUM_STUDENT:
        count +=1

print(count/NUM_EXER)



def factorial(n):
    a = 1
    for i in range(1, n+1):
        a = a*i
    return a

k = 1 - factorial(365)/(factorial(365-NUM_STUDENT)*365**NUM_STUDENT)
print(k)