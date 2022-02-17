
def happiness (n,m,a,b):
    happ = 0
    for val in a:
        if val in array:
            happ+=1
    for val in b:
        if val in array:
            happ-=1

    return happ

if __name__ == '__main__':
    n,m = [int(x) for x in input().split()]
    array = [int(x) for x in input().split(' ') ]
    a = {int(x) for x in input().split(' ') }
    b = {int(x) for x in input().split(' ') }

    happy = happiness(n,m,a,b)
    print(happy)