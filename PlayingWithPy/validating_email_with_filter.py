import re
def fun(s):
    atSplit = re.split(r"@",s)
    if len(atSplit) == 2:
        #print("pass")
        userName = atSplit[0]
        extSplit = re.split(r"\.",atSplit[1])
        if len(extSplit)==2:
            #print("pass")
            at = extSplit[0]
            ext = extSplit[1]
            if len(ext)<=3 and ext.isalpha():
                #print("pass")
                #print(at)
                if not re.search(r"[^a-zA-Z0-9]+",at):
                    #print("pass")
                    if not re.search(r"[^a-zA-Z0-9_-]+",userName) and not userName.strip()=="":
                        #print("----------------")
                        return True
    #print("fail")
    return False
        
        
    
    
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)