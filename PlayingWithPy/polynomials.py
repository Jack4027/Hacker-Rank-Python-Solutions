import numpy as np

if __name__=='__main__':
    coeff = [float(x) for x in input().split()]
    x = float(input())
    print(np.polyval(coeff,x))