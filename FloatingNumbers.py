import re

T = int(input("Enter the number of elements:"))

pattern = r'^[+-]?\d*\.\d+$'

for i in range(T):
    s = input("Enter elements:")

    if re.match(pattern, s):
        print(True)
    else:
        print(False)
