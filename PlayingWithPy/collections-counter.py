# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

if __name__=='__main__':
    Nshoes = int(input())
    wantedSizeAndPrice = []
    shoesizes = input().split(' ')
    
    for i in range(len(shoesizes)):
        shoesizes[i] = int(shoesizes[i])
    Ncust = int(input())
    for i in range(Ncust):
        a,b = input().split(' ')
        a,b = int(a), int(b)
        wantedSizeAndPrice.append([a,b])

    shoeCount = Counter(shoesizes)
    total =0

    for ele in shoeCount.elements():
        for i in wantedSizeAndPrice:
            if ele == i[0]:
                total+=i[1]
                wantedSizeAndPrice.remove(i)
                break
            else:
                None
            
            
    print(total)
        