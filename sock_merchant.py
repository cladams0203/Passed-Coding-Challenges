import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    obj = {}
    count = 0
    for i in ar:
        if i in obj:
            obj[i] += 1
        else:
            obj[i] = 1
    for i in obj:
        count += obj[i] // 2
    print(count)

sockMerchant(50, [10,20,20,10,10,30,50,10,20])