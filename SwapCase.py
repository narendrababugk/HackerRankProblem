def swap_case(s):
    a=s.swapcase()
    return a

if __name__ == '__main__':
    s = input("Enter the string: ")
    result = swap_case(s)
    print("Swapped case string: ")
    print(result)