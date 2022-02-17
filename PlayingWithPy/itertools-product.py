# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ =='__main__':
    
    a = input()
    listA = a.split(' ')
    for i in range(len(listA)):
        listA[i] = int(listA[i])
    
    b= input()
    listB = b.split(' ')
    for i in range(len(listB)):
        listB[i] = int(listB[i])
    
    
    answer = list((product(listA,listB)))
    
    for i in answer:
        if i[0] == ' ' or i[1]==' ':
            None
        else:
            print(i,end = ' ')
    