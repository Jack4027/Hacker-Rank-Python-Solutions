def stringMethod(s1,s2):
    
    if len(s1) == len(s2):
        s1 = sorted(s1)
        s2 = sorted(s2)
        if s1==s2:
            return True
        else:
            return False
    else:
        return False

if __name__=='__main__':
    print(stringMethod('abcdef','decab'))