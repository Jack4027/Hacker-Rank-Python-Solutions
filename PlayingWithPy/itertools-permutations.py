# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

if __name__=='__main__':
    word,number = input().split()
    number = int(number)
    listP = list(permutations(word,number))
    listP = sorted(listP)
    for perm in listP:
        string=''.join(perm)
        print(string)