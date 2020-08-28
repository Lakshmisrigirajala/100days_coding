n=int(input("enter a num:"))
s=int(input("enter starting num:"))
r=int(input("enter ending num:"))
if s<r:
    for i in range(s,r+1):#To print values in increment order
        print(n,"*",i,"=",n*i)
elif r<s:
    for i in range(s,r-1,-1):#To print values in decrement order
        print(n,"*",i,"=",n*i)
