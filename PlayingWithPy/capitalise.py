import os

def solve(s):
    result = ''
    for i in s.split(' '):
        i = i.capitalize()
        result += i+' '
    
    return result
if __name__ == '__main__':
   
    s = input('Enter: ')

    result = solve(s)

    print(result)
