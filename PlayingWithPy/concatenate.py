import numpy as np

if __name__ == '__main__':
    N,M,P = list(map(int,input().split()))
    R = N+M

    array = np.array([],dtype=int)
    for i in range(R):
        array = np.concatenate((array,np.array(list(map(int, input().split())))),axis=0)
        
    print(array)