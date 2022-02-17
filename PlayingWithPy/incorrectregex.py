import re
if __name__=='__main__':
    N = int(input())
    regex = []
    for i in range(N):
        regex.append(input())
    for reg in regex:
        try:
            reg = re.compile(reg)
            isValid = True
        except re.error:
            isValid=False
        print(isValid)