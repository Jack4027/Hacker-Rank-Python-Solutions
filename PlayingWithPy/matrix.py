import math
import os
import random
import re
import sys

#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
string = ''


for index in range(m):
    for chars in matrix:
        string+=chars[index]



redacted = re.sub('([a-zA-Z0-9])[!@#$%&\s]+([a-zA-Z0-9])',r'\g<1> \g<2>',string)

print(redacted)
