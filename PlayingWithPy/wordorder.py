# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    N = int(input())
    words ={}
    for i in range(N):
        word = input()
        if word in words:
            words[word]+= 1
        else:
            words[word]=1
    
    print(len(words.keys()))
    for v in words.values():
        print(v, end=' ')