# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
if __name__=='__main__':
    word, number = input().split()
    number = int(number)
    for i in combinations_with_replacement(sorted(word),number):
        for val in i:
            print(val, end='')
        print() 