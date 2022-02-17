# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=='__main__':
    a = int(input())
    b = int(input())
    answer = divmod(a,b)
    print(answer[0])
    print(answer[1])
    print(answer)