#GCD ==> Greatest Common Divisor
n=int(input("enter a number"))
m=int(input("enter a number"))
s=min(n,m)
for i in range(1,s+1):
    if n%i==0 and m%i==0:
        gcd=i
print(gcd)
