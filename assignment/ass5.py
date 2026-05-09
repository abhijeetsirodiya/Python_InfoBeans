'''1. Smart Voting & ID Verification System
   A government system verifies whether a citizen can vote and whether they have a valid ID.

* If age ≥ 18 → Eligible to vote
* If ID proof is available → Allowed inside booth

Input:
Enter age: 22
Do you have ID (yes/no): yes

Output:
Eligible to vote
Allowed inside booth

a=int(input("Enter age :"))
x=input("Do you have ID (yes/no) :")

if a>=18:
    print("Eligibal to vote")

if x == "yes":
    print("Allowed inside booth")

===============================================2

2. Student Performance Analyzer
   A school wants to evaluate students based on marks.

* If marks ≥ 40 → Pass
* If marks ≥ 75 → Distinction

Input:
Enter marks: 80

Output:
Pass
Distinction

m=int(input("Enter marks:"))

if m>=40:
    print("Pass")

if m>=75:
    print("Distinction")
===================================================3

3. E-Commerce Offer Engine
   An online store provides multiple offers independently:

* If cart value ≥ 500 → Free delivery
* If cart value ≥ 1000 → 10% discount coupon

Input:
Enter cart value: 1200

Output:
Free delivery applied
Discount coupon unlocked
======
c=int(input("Enter cart value:"))

if c>=500:
    print("Free delivery")
if c>=1000:
    print("Discount coupon unlocked")
======================================================4
4. Gym Membership Eligibility Checker
   A gym checks multiple conditions:

* If age ≥ 18 → Allowed for gym
* If BMI > 25 → Suggest weight loss program

Input:
Enter age: 25
Enter BMI: 27

Output:
Gym access granted
Enroll in weight loss program

===
a=int(input("Enter age:"))
bmi=int(input("Enter BMI:"))

if a>=18:
    print("Gym access granted")

if bmi>25:
    print("Enroll in weight loss program")
========================================================5

5. Banking Security System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password

Input:
Enter username: admin
Enter password: secure123

Output:
Valid user
Strong password
====

ad=input("Enter username:")
p=(input("Enter password:"))

if ad=="admin":
    print("Valid user")
if len(p)>=8:
    print("Strong password")

===================================================6
6. Weather Monitoring System
   A system checks weather conditions:

* If temperature ≥ 30 → Hot day
* If humidity ≥ 70 → High humidity alert

Input:
Enter temperature: 32
Enter humidity: 75

Output:
Hot day
High humidity alert

===

t=int(input("Enter temprature:"))
h=int(input("Enter humidity:"))

if t>=30:
    print("Hot day")

if h>=70:
    print("High humadity alert")

==================================================7

7. Salary Benefits System
   A company provides benefits:

* If salary ≥ 30000 → Eligible for PF
* If salary ≥ 50000 → Eligible for bonus

Input:
Enter salary: 55000

Output:
PF applicable
Bonus applicable

===

s=int(input("Enter salary:"))

if s>=30000:
    print("PF applicable")
if s>=50000:
    print("Bonus applicable")
============================================8
8. Number Property Checker
   A system evaluates number properties:

* If number % 2 == 0 → Even number
* If number % 5 == 0 → Divisible by 5

Input:
Enter number: 20

Output:
Even number
Divisible by 5
===

n=int(input("Enter number:"))

if n%2==0:
    print("Even number")

if n%5==0:
    print("Divisible by 5")
=============================================9


9. Library Access System
   A library checks:

* If membership is active → Entry allowed
* If books issued < 3 → Can issue more books

Input:
Membership active (yes/no): yes
Books issued: 2

Output:
Entry allowed
Can issue more books
====

x=input("Membership active (yes/no):")
y=int(input("Book issued:"))

if x=="yes":
    print("Entry allowed")

if y<3:
    print("Can issue more books")
====================================================10

10. Online Exam System
    System evaluates exam conditions:

* If marks ≥ 40 → Pass
* If attendance ≥ 75 → Eligible for certificate

Input:
Enter marks: 60
Enter attendance: 80

Output:
Pass
Eligible for certificate

===

m=int(input("Enter marks:"))

if m>=40:
    print("Pass")

if m>=75:
    print("Eligible for certificate")

'''



















