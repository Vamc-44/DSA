#Prinitng all the divisors of the number

def Divisor(N):
    N = abs(N)  
    divisors = []
    for i in range(1, N + 1):
        if N % i == 0:
            divisors.append(i)
    return divisors

Divisor(36)
Divisor(9)