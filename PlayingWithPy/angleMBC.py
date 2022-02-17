# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 
if __name__=='__main__':
    sideAB = int(input())
    sideBC = int(input())
    
    sideAC = (sideAB**2)+(sideBC**2)
    sideAC = sideAC**0.5

    sideMC = sideAC/2
    angelbcmR = math.asin(sideAB/sideAC)
    angelbcmD = math.degrees(angelbcmR)
    
    #c2 = a2 + b2 - 2ab cos C
    sideBM = (sideBC**2)+(sideMC**2)-(2*sideBC*sideMC*math.cos(angelbcmR))
    sideBM = sideBM**0.5
    
    #a / sin A = b / sin B = c / sin C
    temp = sideBM/(math.sin(angelbcmR))
    temp = sideMC/temp
    target = math.asin(temp)
    target = math.degrees(target)
    
    degree_sign = u"\N{DEGREE SIGN}"
    print(str(int(round(target)))+str(degree_sign))