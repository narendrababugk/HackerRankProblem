from itertools import combinations
print("Enter the number of test cases:")
t = int(input())

for _ in range(t):
    print("Enter the number of elements in set A:")
    na = int(input())
    print("Enter the elements of set A:")
    a = set(map(int, input().split()))
    
    print("Enter the number of elements in set B:")
    nb = int(input())
    print("Enter the elements of set B:")
    b = set(map(int, input().split()))
    print("Is set A a subset of set B?")
    print(a.issubset(b))