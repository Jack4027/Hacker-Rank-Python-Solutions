if __name__=='__main__':
    n = int(input())
    s = set(map(int, input().split()))

    N = int(input())
    for i in range(N):
        values = input().split()
        if len(values)>1:
            instruction,number = values[0],int(values[-1])
        else:
            instruction = values[0]
        
        if instruction=='pop':
            s.pop()
        elif instruction=='remove':
            if number not in s:
                continue
            else:
                s.remove(number)
        elif instruction =='discard':
            s.discard(number)
    
    print(sum(s))