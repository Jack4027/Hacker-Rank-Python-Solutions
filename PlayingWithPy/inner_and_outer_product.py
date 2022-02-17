import numpy as np

if __name__ =='__main__':
    
    A = np.array([int(x) for x in input().split()])
    B = np.array([int(x) for x in input().split()])
    print(np.inner(A,B))
    print(np.outer(A,B))