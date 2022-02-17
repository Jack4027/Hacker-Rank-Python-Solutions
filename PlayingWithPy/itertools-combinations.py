# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
if __name__=='__main__':
    a,b = input().split(' ')
    b = int(b)
    for i in range(1,b+1):
        for j in combinations(sorted(a),i):
            for val in j:
                print(val, end='')
            print()