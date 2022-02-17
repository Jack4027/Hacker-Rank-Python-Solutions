# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
    
if __name__=="__main__":
    N = int(input())
    string = ""
    for _ in range(N):
        string+=input()+"\n"
    string = re.sub(r"\s[&]{2}\s"," and ",string)
    string = re.sub(r"\s[&]{2}\s"," and ",string)

    string = re.sub(r"\s[|]{2}\s"," or ",string)
    string = re.sub(r"\s[|]{2}\s"," or ",string)

    
    print(string)