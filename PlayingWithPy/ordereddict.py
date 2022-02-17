from collections import OrderedDict

if __name__=='__main__':
    orddict = OrderedDict()
    N = int(input())
    for i in range(N):
        a = input().split(' ')
        b = int(a.pop(-1))
        a = ' '.join(a)
        
        if a not in orddict:
            orddict[a] = b
        else:
            orddict[a]+=b
    for k,v in orddict.items():
        print(k,v)