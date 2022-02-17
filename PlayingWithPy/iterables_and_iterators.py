# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product, combinations
if __name__=='__main__':
    N = int(input())
    letters = input().split()
    K= int(input())
    combos = combinations(letters, K)
    count = 0 
    length = 0
    for combo in combos:
        if 'a' in combo:
            count+=1
        length+=1
    
    answer = (count/length)
    
    print(answer)
        