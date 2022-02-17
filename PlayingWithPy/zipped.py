# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=='__main__':
    N,X = map(int, input().split())
    marks = []
    for i in range(X):
        marks+= list(map(float, input().split()))

    student = N
    for n in range(N):
        
        studentScores = marks[n::student]
        total = 0
        for s in studentScores:
            total+=s
        average = total/X
        print(average)