#Whether the number is Armstrong or not
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
def Armstrong(N):
    temp=N
    sum=0
    while(temp>0):
        digit=temp%10
        sum=sum+digit**countdigits(N)
        temp=temp//10
    if(N==sum):
        print(N, "is an Armstrong number")
    else:
        print(N, "is Not an Armstrong number")

Armstrong(153)  
Armstrong(1634) 
Armstrong(1633)