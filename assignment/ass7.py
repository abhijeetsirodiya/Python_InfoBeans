'''
1. Electricity Department Billing System


The electricity department of a city wants to automate the monthly bill generation process for its customers. The bill is calculated based on slab-wise unit consumption:

* First 100 units are charged at ₹5 per unit
* Next 100 units (101–200) are charged at ₹7 per unit
* Units above 200 are charged at ₹10 per unit

Write a Python program to calculate the total electricity bill based on the number of units consumed.

Input:
Enter units consumed: 250

Output:
Total Electricity Bill: ₹1950
=
u=int(input("Enter unit consumed: "))
                                                             
if u<=100:
    a=(u*5)
    print("100 vali:",a)
elif u>100 and u<=200:
    c=(u*7)
    print("200 se kam:",c)
else:
   if u>=200:
       d=(u*10)
       print("200 se upar:",d)
       e=(a+c+d)
       print("Total Electricity Bill:",e)
print("Exit")

u=int(input("Enter Unit  :"))
a=(u-200)
b=(a*10)
print("a",b)
c=((u-a)/2)
d=(c*7)
print("b",d)
e=(c*5)
print("Toal Electricity Bill:",(b+d+e))



2. College Result Processing System


A college wants to generate grades for students automatically based on their marks in an exam. The grading criteria are as follows:

* 90 and above → Grade A
* 75 to 89 → Grade B
* 60 to 74 → Grade C
* 50 to 59 → Grade D
* Below 50 → Fail

Write a Python program to display the grade of a student.

Input:
Enter marks: 67

Output:
Grade: C

m=int(input("Enter marks:"))

if m<50:
    print("Fail")
if m>=50 and m<=59:
    print("Grade D")
if m>=60 and m<=74:
    print("Grade C")
if m>=75 and m<=89:
    print("Grade B")
if m>=90:
    print("Grade A")

=====================================================================3


3. Income Tax Department System

The Income Tax Department needs a system to calculate tax payable by citizens based on their annual income:

* Up to ₹2,50,000 → No tax
* ₹2,50,001 to ₹5,00,000 → 5% tax
* ₹5,00,001 to ₹10,00,000 → 20% tax
* Above ₹10,00,000 → 30% tax

Write a Python program to calculate the tax amount.

Input:
Enter annual income: 800000

Output:
                                                          [error]
Tax Payable: ₹110000

i=int(input("Enter annual income: "))

if i<=250000:
    print("No tax")
elif i>=250001 and i<=500000:
    a=((i*5)/100)
    print("tax payable:",a)
elif i>=50000 and i<=1000000:
    b=((i*20)/100)
    print("Tax Payble:",b)
elif i>=1000000:
    print((i*30)/100)
    print("Tax Payable:",c)

========================================================4
4. E-Commerce Discount Engine


An online shopping platform provides discounts to customers based on their total purchase amount:

* Above ₹5000 → 20% discount
* ₹2000 to ₹5000 → 10% discount
* Below ₹2000 → 5% discount

Write a Python program to calculate the final amount after discount.

Input:
Enter purchase amount: 4500                                                    [error]
Output:
Final Amount: ₹4050
'''
i=int(input("Enter purchase amount:"))

if i>=5000:
    if i>=2000 and i<=5000:
        b=i-(i*0.20)
    elif i<2000:
            b=i-(i*0.10) 
else:
    if i<=2000:
        b=i-(i*0.05)
print("Final Amount:",b)
'''
====================================================================5

5. Cinema Ticket Booking System


A cinema hall charges ticket prices based on the age of the customer:

* Children (below 12 years) → ₹100
* Adults (12 to 60 years) → ₹200
* Senior citizens (above 60 years) → ₹150

Write a Python program to determine the ticket price.

Input:
Enter age: 10

Output:
Ticket Price: ₹100
===

a=int(input("Enter age:"))

if a<=12:
    print("Ticket Price:100")
if a>=12 and a<=60:
    print("Ticket Price:200")
if a>60:
    print("Ticket Price:150")

==========================================================6
  

6. Company Bonus Distribution System


A company wants to calculate bonuses for employees based on their years of experience:

* More than 10 years → 20% bonus
* 5 to 10 years → 10% bonus
* 2 to 5 years → 5% bonus
* Less than 2 years → No bonus

Write a Python program to calculate the bonus amount.

Input:
Enter salary: 50000
Enter years of experience: 6
                                                               [Error]
Output:
Bonus Amount: ₹5000
=====

s=int(input("Enter salary:"))
a=int(input("Enter years of experience:"))

if a>10:
    d=(s*20/100)
    print("Bonus Amount:",d)
elif a>=5 and a<=10:
    c=(s*10/100)
elif a>=2 and a<=5:
    b=((s*5)/100)
    print("Bonus Amount:",b)
elif a<=2:
    print("No bonus")
else:
    print("exit")

=====================================================7
7. Banking Withdrawal Limit System


A bank wants to set withdrawal limits based on the available account balance:

* Balance less than ₹1000 → Withdrawal not allowed
* ₹1000 to ₹5000 → Maximum withdrawal ₹1000
* Above ₹5000 → Maximum withdrawal ₹5000

Write a Python program to display the withdrawal limit.

Input:
Enter account balance: 3500

Output:
Maximum Withdrawal Limit: ₹100

a=int(input("Enter account balance:"))
if a<1000:
    print("Withdrawal not allowed")
if a<5000 and a>1000:
    print("Maximum withdrawal:1000")     
if a>5000:
    print("Maximum withdrawal :5000")
  
===========================================================8

8. Weather Monitoring System

A weather monitoring system classifies the weather condition based on temperature:

* Below 0°C → Freezing
* 0°C to 20°C → Cold
* 21°C to 35°C → Warm
* Above 35°C → Hot

Write a Python program to classify the weather.

Input:
Enter temperature: 38

Output:
Weather Condition: Hot
===

t=int(input("Enter temperature:"))

if t>35:
    print("Weather Condition:Hot") 
if t>21 and t<35:
    print("Weather Condition:Warm")
if t>0 and t<20:
    print("Weather Condition:cold")
if t<0:
    print("Weather Condition:Freezing")

=========================================================9


9. Student Attendance Eligibility System

A college determines whether a student is eligible to sit for exams based on attendance percentage:

* 75% and above → Eligible
* 60% to 74% → Eligible with warning
* Below 60% → Not eligible

Write a Python program to check eligibility.

Input:
Enter attendance percentage: 58

Output:
Status: Not Eligible

p=int(input("Enter attendance percentage:"))

if p>=75:
    print("Status:Eligible")
if p>=60 and p<=74:
    print("Status:Eligible with warning")
if p<60:
    print("Status:Not eligible")

=======================================================10

10. Mobile Data Plan Advisor


A telecom company suggests the most suitable data plan based on a user’s daily data usage:

* More than 3GB/day → Premium Plan
* 1GB to 3GB/day → Standard Plan
* Less than 1GB/day → Basic Plan

Write a Python program to recommend a plan.

Input:
Enter daily data usage: 0.8

Output:
Recommended Plan: Basic Plan

e=float(input("Enter daily data usage:"))

if e>3:
    print("Recommended Plan:Preminm Plan")
if e>1 and e<3:
    print("Recommended Plan:Standard Plan")
if e<1:
    print("Recommended Plan:Basic Plan")

==================================================11
11. Railway Ticket Fare System


A railway system calculates ticket fare based on distance and travel class:

* Distance ≤100 km:
  Sleeper → ₹100, AC → ₹200
* Distance 101–500 km:
  Sleeper → ₹300, AC → ₹600
* Distance >500 km:
  Sleeper → ₹500, AC → ₹1000

Write a Python program to calculate ticket fare.

Input:
Enter distance: 350
Enter class: AC

Output:
Total Fare: ₹600
==

d=int(input("Enter distance:"))
a=input("Enter class:").lower()

if d<=100:
    if a=='ac':
        print("Total Fare :200")
    else:
        print("Total Fare :100")
if d>=101 and d<=500:
    if a=='ac':
        print("Total Fare :600")
    else:
        print("Total Fare :300")
if d>=500:
    if a=='ac':
        print("Total Fare :1000")
    else:
        print("Total Fare :500")

================================================12
12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000
                                                       [error]
Output:
Final Bill Amount: ₹4680
===

b=int(input("Enter bill amount:"))

if b>=5000:
    a=((b*18)/100 +200)
    print("Finall Bill Amount:",a+b)
if b>=1001 and b<=3000:
    if b>=3000 and b<=5000:
        c=((b*12)/100+200)
        print("Final Bill Amount:",b+c)
else:
    if b>=1001 and b<3000:
        f=((b*12)/100)
        print("Final Bill Amount:",b+f)
        
if b<=1000:
    d=((b*5)/100)
    print("Final Bill Amount:",b+d)

==========================================13
13. Employee Performance Appraisal System


A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
  If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 18000
Enter rating: 4

Output:
Revised Salary: ₹23600
==

s=int(input("Enter salary:"))
r=int(input("Enter rating:"))
if r==5:
    if s<20000:
       s=s+2000+(s*0.25)
    else:
       s=s+(s*0.25)    
if r==4:
    if s<20000:
       s=s+2000+(s*0.20)
    else:
       s=s+(s*0.20)
if r==3:
    s=s+(s*0.1)
if r==2:
    s=s+(s*0.05)
if r==1:
    print("No hike")
print("Revised Salary:",s)

==========================================14
14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount                             
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000
====

t=input("Enter course catagory:")
u=input("Enter user type:")

if t=='programming':
    if u=='student':
        a=5000-(5000*0.2)
        
    elif u=='working':
        a=5000-(5000*0.1)
       
    else:
        if u=='other':
          a=5000   

elif t=='design':
    if u=='student':
        a=4000-(4000*0.2)
    elif u=='working':
        a=4000-(4000*0.1)
        
    else:
        if u=='other':
            a=4000 
elif t=='marketing':
    if u=='student':
        a=3000-(3000*0.2)
    elif u=='working':
        a=3000-(3000*0.1)
    else:
        if u=='other':
           a=3000
print("Final course Fee:",a)

=============================================15

15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220
===

t=input("Enter vehicle type:")
p=int(input("Enter hours parked:"))
if t=='bike':
    if p>5:
        x=((p*10)+100)
        print("Total Parking fee:",x)
    else:
        y=(p*10)
        print("Total Parking fee:",y)
if t=='car':
    if p>5:
        q=((p*20)+100)
        print("Total Parking fee:",q)
    else:
        r=(p*20)
        print("Total Parking fee:",r)
if t=='bus':
     if p>5:
         u=((p*20)+100)
         print("Total Parking fee:",u)
     else:
         v=(p*50)
         print("Total Parking fee:",v)

==========================================================end

t=input("Enter vehicle type:").lower()
p=int(input("Enter hours parked:"))

if t=='bike':
    if p>5:
        x=((p*10)+100)
    else:
        x=(p*10)
elif t=='car':
    if p>5:
        x=((p*20)+100)
    else:
        x=(p*20)
elif t=='bus':
    if p>5:
        x=((p*50)+100)
    else:
        x=(p*50)
print("Total fees ",x)
'''     







