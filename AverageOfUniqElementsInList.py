def average(array):
    s = set(array)          
    total = sum(s)          
    length = len(s)         
    return total / length
   

print("Enter the number of elements in the array: ")
n = int(input())
print("Enter the elements of the array: ")
arr = list(map(int, input().split()))
result = average(arr)
print("Average of unique elements:")
print(result)