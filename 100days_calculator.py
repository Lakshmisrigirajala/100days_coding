def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
if __name__=="__main__":
    a=int(input("enter a value:"))
    b=int(input("enter b value:"))
    p=(input("Choose +,-,*,/:"))
    if p=="+":
        print(add(a,b))
    elif p=="-":
        print(sub(a,b))
    elif p=="*":
        print(mul(a,b))
    elif p=="/":
        print(div(a,b))
