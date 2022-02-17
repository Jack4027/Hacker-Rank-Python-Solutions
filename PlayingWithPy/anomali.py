array = ['a','b','c','d','e','f','g']


for k,v in enumerate(array):
    
    if k > len(array)/2 - 1:
        break

    temp =array[-k-1]
    array[-k-1] = array[k]
    array[k] = temp

print(array)
    
    