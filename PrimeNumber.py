#Give number is a prime number or not

n=int(input())
def prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

if prime(n):
    print("prime")
else:
    print("not a prime")