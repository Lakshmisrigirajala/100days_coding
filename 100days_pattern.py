#General Method ==> ABCDE-5times
a="ABCDE"
for i in a:
    print(a,end="\n")

print()

#ASCII Model ==> ABCDE-5times
for i in range(5):
    for j in range(5):
        print(chr(j+65),end="")
    print()


#ASCII Model ==> ABCDEFGHIJKL........
a=int(input())
for i in range(a+1):
    print(chr(i+65),end="")
