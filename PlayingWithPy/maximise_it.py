# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
if __name__ =='__main__':
    K,M = map(int, input().split())
    lines = []
    for i in range(K):
        temp = list(map(int, input().split()))
        temp = temp[1: ]
        lines.append(temp)
    combos = product(*lines)
    #S(max) = (X1** + X2** ......+ XK**)%M
    maxi = 0
    for combo in combos:

        temp = 0
        for i in combo:
            temp+=i**2
        temp = temp%M
        
        if temp >= maxi:
            maxi = temp
        else:
            None
    
    print(int(maxi))
        