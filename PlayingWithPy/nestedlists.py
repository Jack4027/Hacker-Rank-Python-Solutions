if __name__ == '__main__':

     students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
     lowest = float('inf')
     name = []
     scores_ND = {i[1] for i in students}
     scores_ND = list(scores_ND)
     scores_ND.sort()
     secLow = scores_ND[1]
     names = [i[0] for i in students if i[1] == secLow]

     print(names)
        
    