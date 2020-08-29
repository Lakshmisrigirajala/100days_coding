#5
#2 3 5
#1 2 3-->positions
#5 is a superprime as its index 3 is prime
import math
def prime(n):#11
    if n>1:
        for i in range(2,abs(int(math.sqrt(n)))+1):
            if n%i==0:
                return 2
                break
        else:
            return 1
    else:
        return 2
def super_prime(n):#11
    l=[]
    for i in range(2,n+1):# 2 to 12
        if prime(i)==1:#2,3,5,7,11
            l.append(i)
            i+=1
    list1=l#[2,3,5,7,11]
    m=len(list1)#5
    if prime(m)==1:
        return(2)
    else:
        return(3)
n=int(input())
if prime(n)==1:
    if super_prime(n)==2:
        print(n," is a superprime")
    else:
        print(n," is not a superprime")
elif prime(n)==2:
    print(n," is not a prime")
