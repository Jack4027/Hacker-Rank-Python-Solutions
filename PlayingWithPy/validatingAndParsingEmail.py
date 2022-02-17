# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils as email

if __name__=="__main__":
    N = int(input())
    valids = []
    for _ in range(N):
        e = email.parseaddr(input())
        
        if re.fullmatch(r"[A-Za-z]{1}[A-Za-z0-9-_.,]*[@]{1}[A-Za-z]+[.]{1}[A-Za-z]{0,3}",e[1]):
            valids.append(email.formataddr(e))
    
    for v in valids:
        print(v)
            