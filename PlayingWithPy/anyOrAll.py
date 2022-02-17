# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=="__main__":
    N,numbers= int(input()),[int(x) for x in input().split(' ')]
    print(all(map(lambda x: x>0, numbers)) and any(map(lambda x: str(x)==str(x)[::-1],numbers)))
