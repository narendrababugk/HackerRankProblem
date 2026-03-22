import textwrap

def wrap(string, max_width):
    s=textwrap.fill(string,max_width)
    return s

if __name__ == '__main__':
    string= input("Enter the string: ")
    max_width =int(input("Enter the maximum width: "))
    result = wrap(string, max_width)
    print("Wrapped string: ")
    print(result)