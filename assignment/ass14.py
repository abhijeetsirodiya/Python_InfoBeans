'''
1. Triple Operation Prime Verification System

A cybersecurity company generates a security score from entered access code.

Write a program to:

- Find sum of digits of the number
- Reverse the number
- Find absolute difference between original number and reverse
- Add digit sum and difference
- Check whether final result is Prime or Not Prime

Input:
4215

Output:
Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime
===

n=int(input("Input:"))
temp=n
s=0
reverse=0
i=1
while i<=n:
    a=n%10
    s= s + a
    reverse=reverse*10+a
    i+=1
    n=n//10
   
print("Sum of Digits = ",s)
print("Reverse = ",reverse)
difference=(reverse-temp)
print("Difference = ",difference)
f=(difference+s)
print("Final Result = ",f)
i=0
if i<=1:
    print("Not Prime")
else:
    for i in range(2,f):
        if f%i==0:
            print("not Prime")
            break
    else:
        print("Prime")

=============================================================================2

2. Multi Stage Prime Lock System

A smart locker opens only if final derived number is prime.

Write a program to:

- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not

Input:
234

Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime
=======

n=int(input("Input:"))

sum=0
i=1
count=0
product=1
while n>0:
    a=n%10
    sum=sum+a
    product=product*a
    difference=product-sum
    i=1
    while difference>0: 
        digit=difference%10
        count=count+digit
        i+=1
        difference=difference//10
    f=difference+count
    i+=1
    n=n//10
print("Sum =",sum)
print("Product =",product)
print("Difference =",difference)
print("Digit =",digit)
print("Final result =",f)

if f<=1:
    print ("Not prime")
else:
    while i>0:
        if f%i==0:
            print("Not prime")
        i+=1
    else:
        print("Prime")

=================================================================3

3. Perfect Number Reward System

A gaming company rewards users if entered number is a Perfect Number.

(Perfect Number = sum of proper factors equals number)

Write a program using for-else loop to:

- Find sum of proper factors
- If sum equals number print Reward Unlocked
- Else print Try Again

Input:
6

Output:
Reward Unlocked
===

n=int(input("Input:"))
i=1
sum=0
for i in range(1,n+1):
    if n%i==0:
        print("Reward Unlock")
        break
else:
    print("Try Again")

===================================================================4

4.Unique Digit Security Scanner

A smart locker accepts only numbers whose all digits are unique.

Write a program using for-else loop to:

- Check every digit
- If any repeated digit found reject
- Else accept

Input:
57294

Output:
Valid Unique Code
===

n=int(input("Input:"))

while n>0:
    a=n%10
    n=n//10
    a1=n%10
    if a==a1:
        print("reject")
        break
    n=n//10
else:
    print("Valid Unique Code")

=====================================================================5

5.Number Stability Analyzer

A science lab studies whether digits are in increasing order.

Write a program using for-else loop:

- If every next digit is greater than previous print Stable Number
- Else Unstable Number

Input:
12359

Output:
Stable Number
===

n=int(input("Input:"))
a=1
for i in range(1,n+1):
    if a>=i:
        a=i
        print(a)
        print("Stable Number")
    break
else:
    print("Unstable Number")

=======================================================================6
         
6.
Next Prime Cabin Number Generator

A luxury hotel gives only prime numbered cabins to VIP guests.

Manager enters the last allotted cabin number.
System must find the next available prime cabin number.

Write a program using loops.

Input:
24

Output:
Next Prime Cabin = 29
===

   
=======================================================================7
  
7.
 Alternate Digit Prime Checker

A math lab adds alternate digits from right side.

Write a program to:

- Find sum of alternate digits
- Check whether sum is Prime or Not

Input:
12345

Output:
Alternate Sum = 9
Not Prime
===

n=int(input("Input:"))
temp=n
sum=0
for i in range(1,n,1):
    sum=sum+i
    print("Alternate Sum =",sum)
sum=f
if f<=1:
    print ("Not prime")
else:
    while f>0:
         if f%i==0:
              print("Not prime")
         i+=1
    else:
         print("Prime")

=========================================================================8

8.
 ATM Note Counter

A bank ATM dispenses ₹100 notes.

Write a program to:

- Read withdrawal amount
- Count how many ₹100 notes needed using loop

Input:
700

Output:
Notes = 7
===

n=int(input("Input: ="))

for i in range(1,n+1):
    a=n//100
    print("Notes =",a)
    break

=========================================================================9

9.
 Bike Service Kilometer Checker

A bike needs service every 3000 km.

Write a program to:

- Read travelled kilometers
- Print every service checkpoint till entered km

Input:
10000

Output:
3000 6000 9000
===

import math
n=int(input("Input: ="))
i=1
for i in range(0,n,3000):
    print(i , end=" ")
    

==========================================================================10

  10.
Lift Mode Operation – Advanced Smart Elevator System

A smart building elevator works in multiple intelligent modes based on the mode number entered by the control panel.  
The system must automatically execute floor movement instructions using loops.

Write a program:

- If mode = 1  
  Normal Up Mode activated.  
  Read current floor and destination floor.  
  Print all floors from current to destination in ascending order.

- Else if mode = 2  
  Down Mode activated.  
  Read current floor and destination floor.  
  Print all floors from current to destination in descending order.

- Else if mode = 3  
  Energy Saving Mode activated.  
  Read destination floor.  
  Lift starts from ground floor (0) and stops only on alternate floors till destination.

- Else  
  Emergency Mode activated.  
  Print "Emergency Alarm" 4 times using loop.

Input:
3
6

Output:
0 2 4 6


Input:
1
2
7

Output:
2 3 4 5 6 7


Input:
2
8
3

Output:
8 7 6 5 4 3


Input:
5

Output:
Emergency Alarm
Emergency Alarm
Emergency Alarm
Emergency Alarm  
    
'''
mode=int(input("Input ="))
n1=int(input(""))
n2=int(input(""))

if mode==1:
    if n1<n2:
        for i in range(n1,n2):
            print(i,end=" ")
elif mode==2:
    if n1>n2:
        for i in range(n2,n1,-1):
            print(i,end=" ")
elif mode==3:
    for i in range(0,n):
        if n1 in i:
            continue
else:
    i=1
    while i<=4:
        print("Emergency Alarm")
        i+=1
'''

'''
























