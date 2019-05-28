import math
import os
import random
import re
import sys
from functools import reduce


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sort_arr = sorted(arr)
    arr_1 = sort_arr[0:4]
    arr_2 = sort_arr[-4:]
    print(reduce(lambda x, y: x+y, arr_1), reduce(lambda x, y: x+y, arr_2))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
