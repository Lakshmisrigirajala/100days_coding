#Fibonacci series
n=int(input())
a=0
b=1
print(a,b,end=" ")
for i in range(n):
    c=a+b
    a=b
    b=c
    print(b,end=" ")
