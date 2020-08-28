#LCM ==> Least Common Factor
n=int(input("enter a number"))
m=int(input("enter a number"))
g=max(n,m)
while True:
    if g%n==0 and g%m==0:
        print("lcm=",g)
        break
    g+=1
