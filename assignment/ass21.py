'''
1)	WAP to find out the sum of all integer between 100 and 200 which are divisible by 9

x=int(input("Enter  first number:"))
y=int(input("Enter second number:"))
for i in range(x,y+1):
    n=i 
    if n%9==0:
        print(i)


2)	WAP to print Square, Cube and Square Root of all numbers from 1 to N


n=int(input("Enter the number:"))
for i in range(1,n+1):
    print("Square of the number:",i**2)
    print("Cube :",i**3,"Square root:",i**1/2)


3)	WAP to find out all the leap years between two entered years

x=int(input("Enter starting year:"))
y=int(input("Enter ending year:"))

for i in range(x,y+1):
    if i%4==0 and i%100!=0:
        print(i)


4)
1
00
111
0000
11111

n=int(input("Enter the number:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if i%2==0:
            print(0,end="")
        else:
            print(1,end="")
        j=j+1
    i+=1

6)
a
ab
abc
abcd
abcde

n=int(input("Enter n ="))
i=1
while i<=n:
    print()
    j=1
    ch=97
    while j<=i:
        print(chr(ch),end="")
        j+=1
        ch+=1
    i+=1

   7.
enter n6
     *
    **
   *
  **
 ***
**

n=int(input("Enter n:"))
i=n
while i>=1:
    print()
    dec=i
    while dec>=1:
        print(" ",end="")
        dec-=1 
    s=1
    while s<=i:
        print(" * ",end="")
        s+=1
    inc=i
    while inc<=n:
        print(" ",end="")
        inc+=1
    i-=1

    8.
enter n6
    654321
    65432
     6543
     654
     65
     

n=int(input("Enter n ="))
i=n
while i>=1:
    print()
    inc=i
    while inc<=n:
        print(" ",end="")
        inc+=1
    s=1
    while s<=i:
        print("i ",end="")
        s+=1
    dec=i
    while dec<=1:
        print(" ",end="")
        dec+=1
    
    i-=1

9.
    1
   10
  101
 1010
10101
'''

n=int(input("Enter n="))
i=n
while i>=1:
    print()
    inc=1
    while inc<=i:
        print(" ",end=" ")
        inc+=1
    s=1
    while s<=i:
        print("* ",end="")
        s+=1
    dec=i
    while dec>=1:
        print(" ",end="")
        dec-=1
    i-=1
