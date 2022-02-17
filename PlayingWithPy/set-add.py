# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=='__main__':
    stamps = set()
    
    N = int(input())
    for val in range(N):
        country = input()
        stamps.add(country)
    
    print(len(stamps))