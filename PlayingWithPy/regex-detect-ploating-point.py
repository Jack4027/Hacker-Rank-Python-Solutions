# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
if __name__=="__main__":
    
    for _ in range(int(input())):
        string =input()
        
        if re.search(r"^[+-]?\d*[.]\d+$",string)and not re.search(r"[A-Za-z]+",string):
            print("True")
        else:
            print("False")