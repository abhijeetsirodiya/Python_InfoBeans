'''
1. Product of Odd Numbers up to N

A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.

Input:
5

Output:
15

n=int(input("Input:"))
a=1
for i in range(1,n+1,2):
    a=a*i
print("Output",a)

===============================================================2
2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4

x,y=map(int,input("Input:x , y").split())
count=0
for i in range(x,y):
    if i%7==0:
        count=count+1
print("Output:",count)

==============================================================3

3. Display Numbers Ending with 5

A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.

Input:
10 40

Output:
15 25 35


x,y=map(int,(input("Input:")).split())

for i in range(x,y):
    if i%10==5:
        print(i,end=" ")
================================================================================4


4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number

n=int(input("Input:"))

===============================================================================5

5. Harshad Number Checker

A number scanner is installed in a research laboratory where thousands of numeric access codes are tested every day. To identify mathematically balanced codes, the system checks whether the entered number qualifies as a Harshad number. Numbers passing this test are considered valid for the next stage of processing.

A Harshad number is a number that is exactly divisible by the sum of its digits.

Example:
18 → 1 + 8 = 9 and 18 ÷ 9 = 2

Write a program using loops to check whether the entered number is a Harshad number.

Input:
18

Output:
Harshad Number


n=int(input("Input:"))
s=0
while n>0:
    a=n%10
    s= s+a  
    n=n//10 
     
   
if n%s==0:
    print("Output: Harshad number")
else:
    print("Output: Not Harshad number") 

====================================================================6

6. Automorphic Number Checker

A digital security company designs smart lockers that open only for special self-matching numeric codes. When a user enters a number, the system squares the number and checks whether the result ends with the same digits as the original code. If yes, the locker grants access.

An automorphic number is a number whose square ends with the same number.

Example:
25² = 625

Write a program using loops to check whether the entered number is an Automorphic number.

Input:
25

Output:
Automorphic Number


n=int(input("Input:"))

while n>0:
    a=n**2
    n=n//10
x=n%10
y=a%10
if x==y:
    print("Automorphic Number")
else:
    print("Not ")

=====================================================================7

7. Duck Number Checker

A verification system is used by an e-commerce company to validate promotional coupon numbers. Coupon numbers containing at least one zero in between digits are considered special duck numbers. However, if the number starts with zero, it is rejected immediately.

A duck number is a number that contains at least one zero but does not start with zero.

Example:
1023

Write a program using loops to check whether the entered number is a Duck number.

Input:
1023

Output:
Duck Number
===
'''
n=int(input("Input:"))
y=str(n)
c=0
for i in y:
    if i=="0":
        print("Rejected")
    else:
        rem=n%10
        if rem==0:
            c=c+1
        n=n//10
if c>0:
    print("duck number")
else :
    print("Not duck number")
    
'''



======================================================================8

8.
Mirror Difference Transaction Verification System
A multinational banking company processes thousands of daily transaction IDs. To detect suspicious patterns and validate system-generated IDs,
 the security software performs a Mirror Difference Verification Test.
For every entered transaction ID:

Reverse the digits of the transaction ID

Find the absolute difference between the original ID and the reversed ID


Count the total number of digits in the difference


Apply the following conditions using if-elif-else:

If the difference is 0, print Perfect Match


Else if the difference is divisible by 9, print Verified


Else print Rejected


Write a program to automate this verification process using loops and conditional statements.
Input:
4215
Output:
Reverse = 5124Difference = 909Digits = 3Verified
Input:
1221
Output:
Reverse = 1221Difference = 0Digits = 1Perfect Match
Input:
1234
Output:
Reverse = 4321Difference = 3087Digits = 4Verified

===

i=int(input("Input :"))
count=0
r=0
temp=i
while i>0:
    a=i%10
    r=r*10+a
    i=i//10
n=(r-temp)

if n==0:
    count=count+1
    b=(count,"Prefect match")
print(f"Reverse ={r} Difference ={n} Digits = {b}")
    
elif n%9==0:
    count=count+1
    b=("count,Verified")
print(f"Reverse ={r} Difference ={n} Digits = {b}")

else:
    b=("Rejected")

print(f"Reverse ={r} Difference ={n} Digits = {b}

==========================================================================9


9.
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number


num=int(input("enter num"))
temp=num
t=num%10
num=num//10
rev=0
count=1
while num>0:
    rem=num%10
    k=rem-t
    if k<0:
        k=-k
    rev=rev*10+k
    t=num%10
    count=count+1
    num=num//10
print("total number is",count)
    

sum=0
high=0
fin=0
while rev>0:
    t=rev%10
    if t>high:
        high=t
    sum+=t
    fin=fin*10+t
    rev=rev//10
print("step difference",fin)
print("sum is",sum)
print("highest number is ",high)

if sum//count==0:
    print('balance number')
else:
    print("unbalance number")


'''





















     
     
















