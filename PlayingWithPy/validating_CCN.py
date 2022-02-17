# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def regexFunction(CCN):
    
    if CCN[0]  in ['4','5','6']:
        
        if  re.search(r'\d{5,}[^\d]',CCN) or re.search(r'[a-zA-Z]+',CCN):
            return 'Invalid'
        
        if '-'  in CCN:
            CCN= ''.join(CCN.split('-',4))
       
        
        if len(CCN)!=16 or re.search(r'([0-9])\1{3,}',CCN):
            return 'Invalid'
        else:
            return 'Valid'
    else:
        return 'Invalid'

    
if __name__ == '__main__':
    
    N = int(input())
    
    for i in range(N):
        CCN = input()  
        print(regexFunction(CCN))