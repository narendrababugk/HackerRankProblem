def merge_the_tools(s, k):
    for i in range(0, len(string), k):
        part = string[i:i+k]
        seen = ""
        
        for ch in part:
            if ch not in seen:
                seen += ch
        print(seen)



if __name__ == '__main__':
    string = input("Enter the string:")
    k = int(input("Enter the value of k:"))

    merge_the_tools(string, k)