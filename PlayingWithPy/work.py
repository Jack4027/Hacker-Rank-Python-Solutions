def fizzbuzz(n):
    for i in range(1,n+1):
        if i%3 == i%5==0:
            print('FizzBuzz')
        elif i%3 ==0 and i%5 != 0:
            print('Fizz')
        elif i%3!=0 and i%5==0:
            print('Buzz')
        else:
            print(i)

def toolstrip (tools, start, target):

    indices = []
    [indices.append(i) for i, val in enumerate(tools) if val == target]
    lowest = float('inf')
    for i in indices:
        print(len(tools))
        if i< start:
            temp1 = start - i
            temp2 = len(tools)+i  - start 
            if temp1 >= temp2:
                temp = temp2
            else:
                temp = temp1

        elif start <i:
            temp1 = i - start
            temp2 = len(tools)+start  - i
            if temp1 >= temp2:
                temp = temp2
            else:
                temp = temp1


        if temp<lowest:
            lowest = temp
        
    return lowest 
    
    


if __name__=='__main__':
    #n= int(input().strip())

    tools = ['aaaa','aaaa','bbbb','cccc','dddd','eeee']
    start = 5
    target = 'aaaa'

    print(toolstrip(tools, start, target))
    #fizzbuzz(n)

