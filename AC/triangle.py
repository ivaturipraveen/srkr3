n=int(input())
for i in range(1,n):
    for j in range(n-i):
        print(" ",end="")
    print("*",end=" ")
    for k in range(2,i):
        print(" ",end=" ")
    if i>1:
        print("*",end="")
    print()
for k in range(1,n+1):
    print("*",end=" ")
