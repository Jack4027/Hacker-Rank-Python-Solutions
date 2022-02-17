if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    res = []
    for i in arr:
        if i not in res:
            res.append(i)
    res.sort()
    print(res[-2])
