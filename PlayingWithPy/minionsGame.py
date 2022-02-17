def minion_game(string):
    kevin = ['Kevin',0]
    
    stuart = ['Stuart',0]
    vowels = ['a','e','i','o','u']
    string = string.lower()
    sub = [string[i: j] for i in range(len(string))
     for j in range(i+1, len(string)+1) ]

    substrings = []

    for i in sub:
        if i not in substrings:
            substrings.append(i)

    for i in substrings:
        print(i)
        if i[0] in vowels:
            kevin[1]+= frequencyCount(string,i)
        else:
            stuart[1]+=frequencyCount(string,i)

    if kevin[1] > stuart[1]:
        print('Kevin '+str(kevin[1]))
        print('Stuart '+str(stuart[1]))
    elif stuart[1] > kevin[1]:
        print('Stuart '+str(stuart[1]))
        print('Kevin '+str(kevin[1]))
    else:
        print('Draw')

def frequencyCount(string, substr):
   count = 0
   pos = 0
   while pos < len(string):
       pos = string.find(substr , pos)
       if pos > -1:
           count = count + 1
           pos += 1
       else:
           break
   return count          

if __name__ == '__main__':
    s = 'BANANA'
    
    minion_game(s)