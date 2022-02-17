import string
def print_rangoli(n):
    # your code goes here
    alphabet = string.ascii_letters
    width = (n*4)-3
    numberOfLines = (n*2)-1
    letters = alphabet[n-1::-1]
    whitespace = (2*n)-2
    index=0
    #print(letters[:index])
    midpoint = False
    for _ in range(numberOfLines):
        print('-'*whitespace, end ='')
        middle = letters[:index]+letters[index::-1]
        middle = '-'.join(middle)
        print(middle, end='')
        print('-'*whitespace)
        
        if index == n-1:
            midpoint = True

        if not midpoint:
            index+=1
            whitespace-=2
        else:
            index-=1
            whitespace+=2

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)