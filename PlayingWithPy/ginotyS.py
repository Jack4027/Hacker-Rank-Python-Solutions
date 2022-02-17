# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__=='__main__':
    string = input()
    string = sorted(string)
    odds = []
    evens = []
    capitals = []
    lowers = []
    
    for i in string:
        if i.isupper():
            capitals.append(i)
        elif i.islower():
            lowers.append(i)
        elif int(i)%2 ==0:
            evens.append(i)
        elif int(i)%2 ==1:
            odds.append(i)
    
    newstring = lowers + capitals+odds+evens
    
    print(''.join(newstring))

#Polish Guy solutions

print(*sorted(input(), key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')

print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(), key=order.index), sep='')

import string
print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')
