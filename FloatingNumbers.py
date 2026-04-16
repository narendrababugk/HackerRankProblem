import re

T = int(input())

pattern = r'^[+-]?\d*\.\d+$'

for i in range(T):
    s = input()

    if re.match(pattern, s):
        print(True)
    else:
        print(False)