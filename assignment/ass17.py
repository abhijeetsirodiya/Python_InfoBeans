'''
1. Adjacent Digit Difference Analyzer

A system analyzes differences between consecutive digits in a number.

Write a program to:

Find the difference between every pair of adjacent digits
Display all differences
Count how many differences are even
Find the largest difference
If all differences are same → print Uniform Difference
Else → print Non-Uniform PatternM,MMMMMMM

Input:
84261

Output:
Differences: 4 2 4 5
Even Differences Count = 3
Max Difference = 5
Non-Uniform Pattern

n=int(input("Input:"))
s=0
count=0
len = len(str(n))-1
larg=0
uni = 0
while n>0:
    last1=n%10
    s = s * 10 + last1
    n=n//10


last=s%10
# sub=abs((last)-(((s//10)%10))
sub=abs((last%10)-(last//10))
alldiff=sub

print("Difference = ",end=" ")
while s>9:
    last=s%100
    sub=abs((last%10)-(last//10))
    print(sub,end=" ")
    if sub%2==0:
        count=count+1
    if alldiff == sub:
        uni+=1
    if larg < sub:
        larg = sub
    s=s//10

print("\nEven Difference Count =",count)
print("Max Difference =",larg)
diff=0
if len==uni:
    print("Uniform Difference")
else:
    print("Non Uniform Pattern")

===================================================================2
2. Digit Sum Mirror Checker

A validation system checks symmetry in digit sums.

Write a program to:

Split number into two halves
Find sum of first half digits
Find sum of second half digits
Display both sums
If both sums are equal → print Balanced Number
Else → print Unbalanced Number

Input:
123321

Output:
First Half Sum = 6
Second Half Sum = 6
Balanced Number
=======

n=int(input("Input:"))
t=len(str(n))//2
i=0
right=(n%10**t)
left=(n//10**t)
leftSum = 0
rightSum = 0

while left>0:
    last = left%10
    leftSum = leftSum+last
    left=left//10

print("First half Sum =",leftSum)

while right>0:
    end=right%10
    rightSum = rightSum + end
    right=right//10
    
print("Second Half Sum =",rightSum)

if leftSum==rightSum:
    print("Balance Number")
else:
    print("Unbalance Number")
        

=====================================================================3
 
3.
Digit Neighbor Sum Analyzer

A system analyzes the relationship between a digit and its immediate neighbors.

Write a program to:

Traverse digits from left to right (ignore first and last digit)
For each digit, calculate sum of its adjacent digits
Check if current digit is equal to the sum of its neighbors
Display such digits
Count how many such digits exist
If none found → print No Matching Digit
Else → print Neighbor Sum Pattern Found

Input:
121314

Output:
Matching Digits: 2 3
Count = 2
Neighbor Sum Pattern Found
==


=============================================================4

4.Digit Gap Analyzer

A system analyzes the gap between consecutive digits.

Write a program to:

Traverse digits from left to right
Find the absolute difference between current digit and next digit
Display each difference
Count how many differences are greater than 2
Find the maximum difference
If all differences ≤ 2 → print Smooth Number
Else → print Irregular Pattern

Input:
86421

Output:
Differences: 2 2 2 1
Count (>2) = 0
Max Difference = 2
Smooth Number
'''
n=int(input("Input:"))
s=0
while n>0:
    last=n%10
    s=s*10+last
    n=n//10
print(s)
a=n%10
alldif
























