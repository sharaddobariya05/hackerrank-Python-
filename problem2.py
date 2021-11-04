if __name__ == '__main__':
    n = int(input())
# taken empty string
    string = ""
# from starting index 1 to ending index n, we have concated in the string.
for i in range(1, n+1):
    temp = str(i) 
    string = string + temp
    
print(string)
