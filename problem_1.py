
# technical orientation problem 1 euler's


import pandas as pd
import numpy as num
import matplotlib as plt

sum = 0

for num in range(1,1000):
    if num % 3 == 0:
        sum += num
    elif num % 5 == 0:
        sum += num
    num += 1
print(sum)


