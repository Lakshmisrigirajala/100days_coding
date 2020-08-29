import math
def prime(n):
    for i in range(2,abs(int(math.sqrt(n)))+1):
        if n%i==0:
            break
    else:
        return(1)
n=int(input())
for i in range(n-1,0,-1):
    if prime(i)==1:
        p=i
        break
print(p," is the nearestsmallprime")
i=n+1
while n:
    if prime(i)==1:
        q=i
        break
    i+=1
print(q," is the nearestlargeprime")
if abs(n-p)>abs(n-q):
    print(q," is the nearestprime of ",n)
elif abs(n-p)==abs(n-q):
    print(p,q," are the nearestprime of ",n)
else:
    print(p," is the nearestprime of ",n)
