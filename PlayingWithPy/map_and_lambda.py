cube = lambda x: x**3
def fibonacci(n):
    
    if n >=2:
        fibo = [0,1]
    elif n ==1:
        fibo = [0]   
    else:
        fibo = []
        
    while len(fibo)<n:
        fibo.append(fibo[-2]+fibo[-1])
    
    return fibo
        
        

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))