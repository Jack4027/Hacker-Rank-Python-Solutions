import numpy as np


if __name__ == '__main__':
    values= tuple(map(int,input().split()))
    print(np.zeros(values,dtype=int))
    print(np.ones(values,dtype=int))