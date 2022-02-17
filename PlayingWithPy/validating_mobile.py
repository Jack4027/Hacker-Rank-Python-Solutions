# Enter your code here. Read input from STDIN. Print output to 
if __name__=="__main__":
    N = int(input())
    for _ in range(N):
        string = input()
        if (string.startswith("7") or string.startswith("8") or string.startswith("9")) and len(string)==10 and string.isdecimal():
            print("YES")
        else:
            print("NO") 