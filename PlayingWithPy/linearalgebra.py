import numpy as np

if __name__=='__main__':
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(float, input().split())))
    
    print(round(np.linalg.det(matrix),2))