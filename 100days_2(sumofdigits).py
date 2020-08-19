n=int(input())
m=0
while n>0:
    rem=n%10
    m+=rem
    n=n//10
print(m)
