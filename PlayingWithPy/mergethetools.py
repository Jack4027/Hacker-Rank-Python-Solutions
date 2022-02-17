def merge_the_tools(string, k):
    substrings = [string[i:i+k] for i in range (0,len(string),k)]
    subs = []
    for sub in substrings:
        temp = []
        for let in sub:
            if let not in temp:
                temp.append(let)
        subs.append(temp)
    print(subs)

    for letters in subs:
        for letter in letters:
            print(letter,end=' ')
        print()
        


    
if __name__ == '__main__':
    string, k = 'AAABCADDE', 3
    merge_the_tools(string, k)