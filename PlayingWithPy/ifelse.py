def ifelse (n: int ):
    
    if (n%2 != 0) or (n%2==0 and n>=6 and n<=20):
        print('Weird')

    elif n%2 ==0 and (n<=5 and n>=0) or n>20:
        print('Not Weird')

if __name__== '__main__':

    n = int(input('enter number'))

    ifelse(n)
