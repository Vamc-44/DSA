#count the number of digits in a number
def countdigits(N):
    N = abs(N)  
    count = 0
    if N < 10:
        return 1
    else:
        while N > 0:
            N = N//10
            count += 1
    return count
    
print(countdigits(1234)) 
print(countdigits(1))
print(countdigits(10))
print(countdigits(-5))

import math
def countlogdigits(N):
    if N == 0:
        return 1  # log10(0) is undefined, but 0 has 1 digit
    count = int(math.log10(N)) + 1
    return count

print(countlogdigits(1234))
print(countlogdigits(1))