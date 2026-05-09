n=int(input("Enter n:"))
i=n
while i<=n:
    print()
    inc=1
    while inc<=i:
        print(" ",end="")6
        inc+=1
    space=1
    while space<=(n-i)*2:
        print("*",end="")
        space+=1
    dec=1
    while dec<=i:
        print(" ",end="")
        dec+=1
    i+=1