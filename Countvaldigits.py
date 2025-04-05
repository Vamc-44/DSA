#Sum of digits in a given number
def sumdigits(N):
    N = abs(N)
    sum = 0
    if N < 10:
        return N
    else:
        while N > 0:
            digit = N % 10
            sum += digit
            N = N // 10
        return sum 
    
#Test the function
print(sumdigits(1234)) # 10
print(sumdigits(1))    # 1    
