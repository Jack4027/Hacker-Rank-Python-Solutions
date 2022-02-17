
def loops (n : int):

    for i in range(n):
        print(i**2)

if __name__ == '__main__':
    n = int(input('Enter Number between 1 and 20'))
    loops(n)

