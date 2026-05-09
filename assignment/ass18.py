'''
1. Smart Shopping Mall Discount System
A shopping mall offers discounts based on customer type and purchase amount.
If the customer is premium, they get 20% discount when the amount is more than 5000, otherwise 10%.
If the customer is regular, they get 10% discount when the amount is more than 3000, otherwise 5%.
Write a program to calculate the final payable amount using inline if only.
===========


n=int(input("Enter the amount : "))
user=input("Enter user type :").lower()

x= n-(n*0.2) if user=="premium" and n>5000 else n-(n*0.1) if user=="reglur" and n>3000 else n-(n*0.05)
print("Final amount :",x)

===============================================================================================2

2. University Result Processing System
A university wants to automatically assign grades based on marks.
Marks ≥90 → A+
Marks ≥75 → A
Marks ≥60 → B
Marks ≥50 → C
Below 50 → Fail
Write a program using a single nested inline if expression to display the grade.
========

n=int(input("Enter marks :"))

x= "A+" if n>=90 else "A" if n>=75 else "B" if n>=50 else "C" if n<=50 else "Fail"
print("Grade :",x)

===============================================================================================3

3. Employee Bonus Distribution System
A company provides bonuses based on years of experience.
Experience >10 years → 30% bonus
Experience >5 years → 20% bonus
Otherwise → 10% bonus
Write a program to calculate the total salary after adding bonus using inline if.
==

n=int(input("Enter the salary:"))
exp=int(input("Enter Experience :")) 
x= n+(n*0.3) if exp>10 else n+(n*0.2) if exp>5 else n+(n*0.1)
print("Total Salary:",x)

=============================================================================================4

4.Electricity Billing System
An electricity board calculates bills based on units consumed:
Up to 100 units → ₹5 per unit
101–300 units → ₹7 per unit
Above 300 units → ₹10 per unit
Write a program to compute total bill using inline if.
===

n=int(input("Enter total unit consumed :"))

x= n*5 if n<100 else n*7 if n<300 and n>101 else n*10
print("Total bill :",x)

=============================================================================================5

5.
Calendar System – Leap Year Checker
A digital calendar system needs to check whether a year is a leap year.
A year is a leap year if:

It is divisible by 400, OR
It is divisible by 4 but not by 100
Write a program using inline if to display whether the year is a leap year or not.
===

n=int(input("Enter the Year:"))

x= "Leap year" if (n%400==0) or (n%4==0 and n%100!=0) else "Not A Leap year"

print(x)

==========================================================================================6

6.
Data Validation System – Character Identifier
A system needs to validate user input characters.
If the input is:
Alphabet → display "Alphabet"
Digit → display "Digit"
Otherwise → display "Special Character"
Write a program using inline if to classify the character.
===

n=input(input("Enter the Character:")).lower()

x= "Alphabet" if n in "abcdefghijklmnopqrstuvwxyz"   else "Digit" if n in "0123456789" else "Special Character"

print(x)

'''
n=input(input("Enter the Character:")).lower()

x= "Alphabet" if "a">=n or n<="z"   else "Digit" if n>=0 and n<=9 else "Special Character"

print(x)






































