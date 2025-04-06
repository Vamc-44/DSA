#Finding the GCD or HCF of two numbers

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
      
print(gcd(12, 18)) 
print(gcd(100, 75))