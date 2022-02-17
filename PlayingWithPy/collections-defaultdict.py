# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

if __name__=='__main__':
    sizeA,sizeB = input().split()
    sizeA,sizeB = int(sizeA), int(sizeB)
    dda = defaultdict(list)
    ddb = []
    for i in range(1,sizeA+1):
        dda[(input())].append(i)
    for i in range(sizeB):
        ddb.append(input())
    
    for i in ddb:
        if i not in dda:
            print(-1,end=' ')
        else:            
            for j in dda[i]:
                print(j, end=' ')
        print()