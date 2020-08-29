'''if n=17
      17,13,11,7,5,3,2 are the prime numbers upto 17
check for the sum of each two numbers and add them to 1 to get the result of 17 i.e.,
      17+13+1=31 (!=17)
      13+11+1=25(!=17)
      11+7+1=19(!=17)
      7+5+1=13(!=17)
      Thus, 17 is not a super prime
if n=19
19,17,13,11,7,5,3,2 are the prime numbers upto 19
check for the sum of each two numbers and add them to 1 to get the result of 19i.e.,
      19+17+1=37 (!=19)
      17+13+1=31 (!=19)
      13+11+1=25(!=19)
      11+7+1=19(==19)
      Thus, 19 is a super prime'''
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
def near_prime(n):
    n1=n-1
    while True:
        if prime(n1)==1:
            return n1
        else:
            n1-=1
n=int(input())
if prime(n)==1:
    a=near_prime(n)
    b=near_prime(a)
    while True:
        if a+b+1==n:
            print(a,b)
            print(n," is a special prime")
            break
        else:
            a=b
            b=near_prime(a)
        if a==2 or b==2:
            break
elif prime(n)==2:
    print(n," is not a prime")
            
            
        
