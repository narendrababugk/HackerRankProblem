import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input("Enter the string: ")

    result = solve(s)
    print("Capitalized String: ")
    print(result)

    fptr.write(result + '\n')

    fptr.close()
    def average(array):
    s = set(array)          
    total = sum(s)          
    length = len(s)         
    return total / length
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
    from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in product(a, b):
    print(i, end=' ')
