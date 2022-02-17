if __name__=='__main__':
    N = int(input())
    for _ in range(N):
        try:
            a,b = [int(i) for i in input().split()]
            print(round(a/b))
        except ZeroDivisionError as e:
            print("Error Code: integer division or modulo by zero")
            continue
        except ValueError as e:
            print("Error Code:",e)
            continue