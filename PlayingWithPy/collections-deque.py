# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

if __name__=='__main__':
    N = int(input())
    d = deque()
    for i in range(N):
        values = input().split()
        
        if len(values)>1:
            instruction, number = values[0], values[1]
        else:
            instruction = values[0]
            
        if instruction.lower() == 'append':
            d.append(number)
        elif instruction.lower()=='appendleft':
            d.appendleft(number)
        elif instruction.lower()=='pop':
            d.pop()
        elif instruction.lower()=='popleft':
            d.popleft()
            
    
    for val in d:
        print(val, end = ' ')
