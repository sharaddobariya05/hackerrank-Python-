#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
# 
def plusMinus(arr):
    # Write your code here
    countplus = 0
    countzero = 0
    countmin = 0
    
    for i in range(n):
        if arr[i]>0:
            countplus = countplus+1
            #return countplus
        elif arr[i]==0:
            countzero = countzero+1
            #return countzero
        elif arr[i]<0:
            countmin = countmin+1 
            #return countmin
        else:
            print("No")
        
    proportionplus = countplus/n
    proportionzero = countzero/n
    proportionmin = countmin/n
        
    print(format(proportionplus, ".5f"))
    print(format(proportionmin, ".5f"))
    print(format(proportionzero, ".5f"))

        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    plusMinus(arr)
    
