import numpy as np

if __name__=='__main__':
    N = int(input())
    a = []
    b = []
    
    
    for i in range(N):
       a.append([int(j) for j in input().split()])
    for i in range(N):
       b.append([int(j) for j in input().split()])
    
    a = np.array(a)
    b = np.array(b)
    print(np.dot(a,b))
    print(np.cross(a,b))
        