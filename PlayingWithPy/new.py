
list1 = []
values = ["Height", "Width","Depth"]
for a in range(len(values)):
    b = int(input("enter "+values[a]+" "))

    list1.append(b)


val1,val2,val3 = list1

perimeter = 4*(val1+val2+val3)
volume = val1*val2*val3

print(perimeter)
print(volume) 
