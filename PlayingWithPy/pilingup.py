from collections import deque

if __name__ =='__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        dq = deque(map(int, input().strip().split()))
        
        pile = float('inf')
        while dq:
          num = dq.popleft() if dq[0] > dq[-1] else dq.pop()
          if num > pile: 
            print("No")
            break
          
          pile = num

        if not dq:
            print("Yes")
            
            