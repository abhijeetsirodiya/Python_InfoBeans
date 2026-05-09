'''
1.Digit Product Analyzer System

A data analytics company studies patterns in numeric transaction IDs to detect hidden behaviors.

For every entered number, the system analyzes relationships between its digits.

Write a program to:

Find the product of every pair of adjacent digits
Display all the products
Find the sum of all these products
Find the smallest product value
If the sum of products is divisible by the total number of digits, print Stable Number
Otherwise print Unstable Number

Use loops wherever required.

Input:
57294

Output:
Products: 35 14 18 36
Sum = 103
Smallest = 14
Unstable Number
===

import sys
n=int(input("Input:"))
s=0
sum=0
digit=0
count=0
small= sys.maxsize
while n>0:
    x=n%10
    if x>0:
       count=count+1
    s=s*10+x
    n=n//10
print(s)
print(count)
product=1
while s>1:
    a=s%100
    product=(a//10)*(a%10)
    sum=sum+product
    c=product
    print(product,end=" ")
    s=s//10
    if small>product and 0<product:
        small = product
print("\nSum =",sum)
print("Smallest =",small)

if sum//count==0:
    print("Stable Number")
else:
    print("Unstable Number")


=============================================================================2

2.
Digit Order Break Analyzer

A number validation system checks whether digits of an ID follow a strict increasing pattern. The moment the pattern breaks, the system stops further checking.

Write a program to:

Traverse the digits from left to right
Check whether each digit is greater than the previous digit
If the pattern breaks at any point, stop checking further using break
Display the position where the order breaks (1-based index)
If no break occurs, print Strictly Increasing Number

Use loops and break wherever required.

Input:
12357

Output:
Strictly Increasing Number

Input:
12342

Output:
Break at position = 4
Not Increasing Number
===

import sys
n=int(input("Input:"))
i=0
while n>0:
    x=n%10
    temp=n//10
    if temp%10 < x:
        n=n//10
        i+=1
        n=n//10
    else:
        print("Break at position =",i)
        print("Not Increasing Number")
        break
else:
    print("Strictly increasing number")

===============================================================================3
    
3.
Zero Detection & Early Termination System

A financial system scans transaction IDs digit by digit. If a digit '0' is found, the system immediately stops processing further digits for security reasons.

Write a program to:

Traverse each digit of the number from right to left
Display each digit processed before encountering 0
Stop the loop immediately when 0 is found using break
Count how many digits were processed before termination
If no zero is found, print No Zero Found

Use loops and break wherever required.

Input:
572049

Output:
Digits Processed: 9 4
Count = 2
Zero Found - Process Stopped

Input:
56789

Output:
Digits Processed: 9 8 7 6 5
Count = 5
No Zero Found


n=int(input("Input:"))
count=0
while n>0:
    x=n%10
    if x!=0:
        a=x
        count=count+1
        print("Digits Processed:",a,end=" ")
        print("\nCount =",count)
        n=n//10
    else: 
        print("Digits Processed:",a,end=" ")
        print("\nCount =",count)   
        print("Zero Found - Process Stopped")
        break
else:
    print("Digits Processed:",a,end=" ")
    print("\ncount =",count)
    print("No Zere Found")
        
============================================================4

4.
1. Digit Gap Consistency Checker

A number analysis system checks whether the gap between digits follows a consistent pattern.

Write a program to:

Find the absolute difference between first two digits
Compare this difference with all next adjacent digit differences
If any difference is not equal to the first difference, stop using break
Display:
- Initial gap
- Whether all gaps are same or not

Input:
8642

Output:
Initial Gap = 2
Consistent Pattern

Input:
97531

Output:
Initial Gap = 2
Consistent Pattern

Input:
5321

Output:
Initial Gap = 2
Pattern Break Detected
'''
n=int(input("Input:"))
s=0
while n>0:
    x=n%10
    s=s*10+x
    a=s%100
    sub=(a%10)-(a//10)
    n=n//10
print("Initial Gap =",sub)
if sub==2:
    print("Consistent Pattern")
else:
    print("Pattern Break Detected")

'''
=======================================================================5

5. Digit Alternating Sum System

A coding system calculates alternating sum of digits (add, subtract, add...).

Write a program to:

Traverse digits from left to right
Add first digit, subtract second, add third, and so on
Display final alternating sum
If result is positive → print Positive Pattern
Else → print Negative Pattern

Input:
1234

Output:
Result = -2
Negative Pattern

Input:
8642

Output:
Result = 8
Positive Pattern

num=int(input("Input:"))

i = 1
total=1
n=0
while num>0:
    last = num%10
    n = n*10 + last
    num = num//10

while n>0:
    last = n%10
    if n%2!=0:
        total+=last
    else:
        total-=last
    i+=1
    n=n//10

print(f"Result = {total}")

if total>0:
    print("Positive Pattern")
else:
    print("Negative Pattern")

'''   


  




































        