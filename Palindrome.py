# Reveresing the entered number
N = int(input("Enter a number: "))
def reverse(N):
    N = abs(N)  
    rev = 0
    if N < 10:
        return N
    else:
        while N > 0:
            digit = N % 10
            rev = rev * 10 + digit
            N = N // 10
        return rev

def is_palindrome(N):
    if N == reverse(N):
        return "a Palindrome"
    else:
        return "not a Palindrome"

is_palindrome(N)
print(N,"is", is_palindrome(N))
