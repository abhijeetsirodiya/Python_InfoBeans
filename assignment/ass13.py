
'''
1. Prime Security Code Checker

A high-security research lab uses numeric passcodes to unlock restricted doors. To improve security,
 only prime numbers are accepted because they have exactly two factors and are harder to predict using common patterns.

When an employee enters a code, the system must verify whether the number is prime. If yes, access is granted; otherwise, access is denied.

Write a program to check whether the entered number is Prime or Not Prime.

Input:
29

Output:
Prime Number
===
'''
n=int(input("Input:"))
x=0
if n<=1:
    print("access is denied")

else: 
   i=2
   while i>n:
       if n%i==0:
           x=1
           break
       i+=1
if x==0:
    print("Prime number")
else:
    print("Not a print number")
    
'''
=============================================

2. Next Prime ID Generator

A multinational company auto-generates employee IDs in numeric sequence.
 Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17
====


n=int(input("Input:"))
i=n+1
x=0
y=2
if n<=1:
    print("3")
else:
    
    while true:
        while y<=i//2:
            if i%y==0:
                break
            y=y+1
        if y>i//2:
            print(i)
            break
        i=i+1
         

======================================================================3

3. Composite Number Detector

A product testing company labels batch numbers as risky if they have more than two factors. Such numbers are known as composite numbers and indicate repeated grouping patterns.

The quality control officer enters a batch number, and the software checks whether it is Composite or Not.

Write a program to check whether a number is Composite or Not.

Input:
12

Output:
Composite Number


n=int(input("Input:"))
x=0
i=0
if i<=1:
    print("Composite Number")
else:
    i=2
    while i>n:
        if n%i!=0:
            x=1
            break
    i+=1
if x!=0:
    print("prime")
else:
    print("Composite Number")

=========================================================4

4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31
===

n=int(input("Input:"))











=========================================================5

5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3
===

n=int(input("Input ="))

while


================================================================7
7.
 Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number
===

n=int(input("Input:"))
s=0
for i in range(1,n):
    a = i % 10
    s = s + a
    n = n // 10
print("Sum = ",s)

if i<=1:
    print("Normal number ")
else:
    x=0
    while x>n:
        if n%x==0:
            x=1
    n+=1
if x==0:
    print("Lucky NUmber")
else:
    print("Normal Number")
===============================================================8

8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime

=======


n=int(input("Enter No.:"))
larg=0
small=9
temp=n
while n>0:
    a=n%10
    if larg <= a:
        larg=a
    else:
        small >= a
    n=n//10
print("Largest digit :",larg)
print("smallest digit :",small)

s=0
while temp>0:
    a=n%10
    s=s+a
    temp=temp//10
print("Sum =",s)

i=0
x=0
if i<=1:
    print("Not prime")
else:
    
    while x>0:
        if n%x==0:
            x=1
            break
    n=n//10
if x==0:
    print("Prime")
else:
    print("Not Prime")


==================================================================9

9.Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime


import math
n=int(input("Input:"))
Evencount=0
Oddcount = 0
i=1
while i<=n:
     lst=n%10
     if lst%2=="0":
         Evencount=Evencount+1
         
     else:
         Oddcount=Oddcount+1
     n=n//10
     i+=1

print("Even number =",Evencount)
print("Odd number =",Oddcount)
        
print("Difference = ",abs(Evencount-Oddcount))


          
================================================================10
10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime
===

n=int(input("Input ="))
count=0
s=0
for i in range(0,n):
    if i==0:
        count=count+1
print(s)
print(count)

'''









