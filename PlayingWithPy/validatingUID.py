# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
if __name__ =="__main__":
    N = int(input())
    for _ in range(N):
        result = 'Invalid'
        test = input()
        if len(test) == 10:
            if test.isalnum():
                if re.search(r"\d.*\d.*\d",test):
                    if re.search(r"(.).*\1",test) == None:
                        if re.search(r"[A-Z].*[A-Z]",test):
                            result='Valid'               
        print(result)