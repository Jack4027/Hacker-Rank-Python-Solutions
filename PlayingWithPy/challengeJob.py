import re

    
def func (strParam):

  fstDigit = {}
  secDigit = {}

  for k,v in enumerate(strParam):
    if v in secDigit:
        continue
    if v not in fstDigit:
        secDigit[k] = v
    else:
        fstDigit[k]=v
  
  inbetwDup = []
  for k,v in secDigit.items():
    start = [a for a,b in fstDigit.items() if b==v]
    inbetwDup.append([start,k])

  lengths = []
  for i in inbetwDup:
      check = set()
      check.add([v for v in strParam[i[0]:i[1]]])
      lengths.append(len(check))
  strParam = max()

def StringChallenge(strParam):

  verification = False  
  if len(strParam)>7 and len(strParam)<31:
      strParam.isdecimal()
    if 'password' not in strParam:  
        if strParam.isalnum():
            
            if re.search(r'[+-*!?.,-=@#$%^&*]}{`~/\|:;€><_',strParam):

                if re.search(r'[A-Z]',strParam):
                    verification = True
                    
  print(verification)

  return strParam

# keep this function call here 
print(StringChallenge(input()))