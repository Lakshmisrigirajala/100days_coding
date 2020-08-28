#megaprime==>53 is a prime,....if 5 and 3 are prime,then 53 is called as megaprime
import math
def prime(n):
    if n>1:
        for i in range(2,abs(int(math.sqrt(n)))+1):
            if n%i==0:
                return 2
                break
        else:
            return 1
    else:
        return 2
def mega_prime(m):
    count=0
    while True:
        print("prime")
        rem=m%10
        m=m//10
        if prime(rem)==1:
           count+=1
        rem+=1
        break
    if prime(m)==1 and count==len(str(m)):
        return("megaprime")
    else:
        return("not a megaprime")
n=int(input())
if prime(n)==1:
    print(mega_prime(n))
elif prime(n)==2:
    print("not a prime")
