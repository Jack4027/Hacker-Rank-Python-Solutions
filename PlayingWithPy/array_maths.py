import numpy as np

if __name__ == '__main__':
    
    N,M = list(map(int, input().split()))
    A,B = [],[]
    for i in range(N):
        A.append(list(map(int, input().split())))
    
    for i in range(N):
        B.append(list(map(int, input().split())))
    
    A,B = np.array(A),np.array(B)
    print(A+B)
    print(A-B)
    print(A*B)
    print(np.floor_divide(A,B))
    print(A%B)
    print(A**B)