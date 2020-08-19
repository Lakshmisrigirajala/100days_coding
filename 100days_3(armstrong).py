num=int(input())
arm=0
n=num
while n>0:
    rem=n%10
    arm+=rem**3
    n=n//10
if(arm==num):
    print("armstrong")
else:
    print("not a armstrong")
