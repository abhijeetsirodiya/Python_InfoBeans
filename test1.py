'''

1.Mirror Difference Transaction Verification System
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
====


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

print(f"Reverse ={r} Difference ={n} Digits = {b}")



==========================================================================


2.
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


for i in range(0,n+1):
    sum=sum+i
print("Sum =",sum)

larg=0
while n>0:
    a=n%10
    if larg <= a:
        larg=a
    n=n//10
print("Largest digit :",larg)

===============================================================1

1.
Digit Frequency Balance Analyzer

A data security system analyzes numeric IDs to check digit distribution patterns.

For a given number, the system evaluates how frequently each digit appears.

Write a program to:

Count how many times each digit appears in the number
Display only the digits that appear more than once
Find the total count of repeated digits
Find the digit with maximum frequency
If no digit repeats, print Unique Number
If at least one digit repeats, print Repeated Pattern Detected

Use loops wherever required.

Input:
1223451

Output:
Repeated Digits: 1 2
Total Repeated Count = 4
Max Frequency Digit = 1
Repeated Pattern Detected
===
'''
n=int(input("Input:"))

for i in range(1,n+1):
    digit=n%10
    if i==:
        count=count+1
        print(i)
    n=n//10  
    if i>digit:
        count=count+i
if i!=i:
    

=============================================================================2
2.
Digit Threshold Break Analyzer

A monitoring system analyzes numeric IDs to detect high-value digits. 
The system keeps adding digits one by one, but stops processing as soon as the running sum exceeds a given threshold.

Write a program to:

Accept a number and a threshold value
Traverse digits from right to left
Keep adding digits to a running sum
Display each digit added
The moment sum exceeds the threshold, stop using break
Display:
- Digits processed
- Final sum
- Count of digits processed
If threshold is never exceeded, print Threshold Not Reached

Use loops and break wherever required.

Input:
57294
Threshold = 10

Output:
Digits Processed: 4 9
Sum = 13
Count = 2
Threshold Exceeded

Input:
1234
Threshold = 15

Output:
Digits Processed: 4 3 2 1
Sum = 10
Count = 4
Threshold Not Reached
===
'''
n=int(input("Input:"))
thresh=int(input("Threshold ="))
sum=0
count=0
print("Digit Processed:",end=" ")
while n>0:
    last=n%10
    if sum<thresh:
        sum=sum+last        
        print(last, end = " ")
        count=count+1
    else:
        print("count",count)
        print("Threshold Reached")
        break
    n = n//10

    
















