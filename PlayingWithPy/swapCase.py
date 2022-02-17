def swap_case(s):
    chars = []
    for c in s:
        if c.islower():
           chars.append(c.upper())
        elif c.isupper():
            chars.append(c.lower())
        else:
            chars.append(c)  
    
    return ''.join(chars)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)