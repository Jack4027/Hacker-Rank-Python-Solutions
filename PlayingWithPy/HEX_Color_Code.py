import re
if __name__=="__main__":
    N = int(input())
    selector = False
    for _ in range(N):
        line = input()
        if selector:
            matches = re.findall(r"#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}", line)
            
            for match in matches:
                
                print(match)
        if "{" in line:
            selector = True
        if  "}" in line:
            selector = False
        