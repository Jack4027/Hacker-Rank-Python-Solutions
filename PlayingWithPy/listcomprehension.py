def lc(x,y,z,n):
    print([[a,b,c]for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a+b+c!=n])
if __name__ == '__main__':

    x = int(input('Enter X')) 
    y = int(input('Enter Y')) 
    z = int(input('Enter Z'))
    n = int(input('Enter N'))

    lc (x,y,z,n)