'''
1. Smart Credit Card Approval System

A bank evaluates credit card applications based on income, credit score, employment type, and existing debt.

If income is greater than or equal to 50000, then check credit score. If credit score is greater than or equal to 750, then check debt. If debt is less than 20000, approve Premium Card; otherwise approve Gold Card. If credit score is less than 750, then check employment type. If employment is government and credit score is at least 650, approve Gold Card; otherwise reject.

If income is less than 50000, then check if income is at least 30000 and credit score is at least 700. If yes, approve Silver Card; otherwise reject.

Input:
Income = 45000
Credit Score = 720
Employment = private
Debt = 10000

Output:
Card Type = Silver Card
===

i=int(input("Income ="))
cs=int(input("Credit score ="))
e=input("Employment=").lower()
d=int(input("Debt ="))

if i>=50000:
    if cs>=750:
        if d<=20000:
            print("approve Premium")
        else:
            print("approve Gold card")
    else:
        if e=='government':
            if cs<=750:
                print("approve Gold Card")
            else:
                print("reject")
else:
    if i>=30000 and i<=50000:
        if cs>=700:
            print("Silver Card")
        else:
            print("reject")

==================================================================2
2. Hospital Emergency Priority System

A hospital assigns treatment priority based on age, severity, and insurance.

If severity is critical, then check age. If age is 60 or above, assign Immediate ICU; otherwise assign Emergency Ward.

If severity is moderate, then check insurance. If insured, assign Priority Treatment; otherwise assign General Queue.

If severity is low, then check age. If age is less than 10, assign Pediatric Priority; otherwise assign Wait.

Input:
Age = 65
Severity = critical
Insurance = yes

Output:
Treatment = Immediate ICU
========

a=int(input("Age ="))
s=input("Severity =").lower()
i=input("Insurance =").lower()

if s=='critical':
    if a>=60:
        print("Immediate ICU")
    else:
        print("Emergency Ward")
elif s=='moderate':
    if i=='yes':
        print("Priority Treatement")
    else:
        print("General Queue")

==============================================================3

3. Smart Scholarship Allocation System

A scholarship is provided based on marks, family income, and category.

If marks are 85 or above, then check income. If income is less than or equal to 300000, then check category. If category is not general, give Full Scholarship; otherwise give 75% Scholarship. If income is above 300000, give 50% Scholarship.

If marks are between 70 and 84, then check income. If income is less than or equal to 200000, give 50% Scholarship; otherwise give 25% Scholarship.

If marks are below 70, no scholarship is given.

Input:
Marks = 88
Income = 250000
Category = OBC

Output:
Scholarship = Full Scholarship
===

m=int(input("Marks ="))
i=int(input("Income ="))
c=input("Category =").lower()

if m>=85:
    if i<=300000:
        if c!='general':
            print("Full Scholarship")
        else:
            print("Scholarship = 75% Schalorship")
    else:
        print("Scholarship = 50% Scholarship")
else:
    if m>=70 and m<=84:
        if i<=200000:
            print("Scholarship = 50% Scholarship")
        else:
            print("Scholarship = 25% Scholarship")
    else:
        print("no scholarship is given")

==========================================================
4. Airline Ticket Pricing Engine

An airline calculates ticket price based on class, distance, and booking time.

If class is business, then check distance. If distance is greater than 1000, price is 8000; otherwise 5000.

If class is economy, then check distance. If distance is greater than 1000, then check booking time. If booking is early, price is 4000; otherwise 5000. If distance is less than or equal to 1000, price is 2500.

Input:
Class = economy
Distance = 1200
Booking = early

Output:
Ticket Price = 4000
===

c=input("Class =").lower()
d=int(input("Distance ="))
b=input("Booking =").lower()

if c=='business':
    if d>1000:
        print("Ticket price = 8000")
    else:
        print("Ticket price = 5000")
elif c=='economy':
    if d>1000:
        if b=='early':
            print("Ticket price = 4000")
        else:
            print("Ticket price = 5000")
    else:
        print("Ticket price = 2500")

============================================================5
5. Smart Exam Evaluation System

A student’s result depends on marks, attendance, and internal score.

If marks are 40 or above, then check attendance. If attendance is 75 or above, then check internal marks. If internal is 20 or above, result is Pass; otherwise Grace Pass. If attendance is below 75, result is Detained.

If marks are below 40, then check if marks are at least 35 and internal is at least 25. If yes, result is Reappear; otherwise Fail.

Input:
Marks = 38
Attendance = 80
Internal = 26

Output:
Result = Reappear
===

m=int(input("Marks ="))
a=int(input("Attendence ="))
i=int(input("Internal ="))

if m>=40:
    if a>=75:
        if i>=20:
            print("Result = Pass")
        else:
            print("Result = Grace pass")
    else:
        print("Result = Detained")
else:
    if m>=35 and i>=25:
        print("Result = Reappear")
    else:
        print("Result = Fail")

============================================================6

6. Banking Fraud Detection System

A bank checks fraud risk based on transaction amount, location, device, and transaction count.

If amount is greater than or equal to 50000, then check location. If location is international, then check device. If device is new, then check transaction count. If transactions are more than 3, mark High Risk (Block); otherwise Medium Risk. If device is not new, mark Medium Risk.

If location is domestic, then check transaction count. If more than 5, mark Medium Risk; otherwise Low Risk.

If amount is less than 50000, then check unusual activity. If yes, then check device. If device is new, mark Medium Risk; otherwise Low Risk. If no unusual activity, mark Safe.

Input:
Amount = 70000
Location = international
Device = new
Transactions = 4

Output:
Risk Level = High Risk (Blocked)
===

a=int(input("Amount ="))
l=input("Location =").lower()
d=input("Device =").lower()
t=int(input("Transaction ="))
u=input("User activity yes/no =").lower()

if a>=50000:
    if l=='international':
        if d=='new':
            if t>=3:
                print("High Risk(Block)")
            else:
                print("Medium risk")
        else:
            print("medium risk")
    else:
        if t>=5:
            print("Medium Risk ")
        else:
            print("low risk")
else:
    if a<50000:
        if u=='yes':
            if d=='new':
                print("medium risk")
            else:
                print("low risk")
        else:
            print("safe")

================================================================7

7. University Result Classification System

A university assigns final class based on marks, backlog, and project score.

If marks are 75 or above, then check backlog. If backlog is 0, then check project score. If project score is 80 or above, assign First Class with Distinction; otherwise First Class. If backlog is not 0, assign First Class.

If marks are between 60 and 74, then check backlog. If backlog is less than or equal to 2, assign Second Class; otherwise Pass Class.

If marks are between 50 and 59, assign Pass. Otherwise Fail.

Input:
Marks = 78
Backlogs = 0
Project = 85

Output:
Result = First Class with Distinction
===

m=int(input("Marks ="))
b=int(input("Backlags ="))
p=int(input("Projects ="))

if m>=75:
    if b==0:
        if p>=80:
            print("First class with Distinction ")
        else:
            print("First Class")
    else:
        print("First class")
elif m>=60 and m<=74:
    if b<=2:
        print("Second Class")
    else:
        print("pass class")
elif m>=50 and m<=59:
    print("Pass")
else:
    print("Fail")

========================================================================8


8. E-Commerce Dynamic Pricing System

An e-commerce system gives discount based on demand, stock, user type, and festival.

If demand is 80 or above, then check stock. If stock is less than 50, then check user type. If user is premium, then check festival. If festival is yes, give 20% discount; otherwise 10%. If user is not premium, no discount. If stock is 50 or more, give 5% discount.

If demand is between 40 and 79, then check festival. If yes, give 10% discount; otherwise no discount.

If demand is below 40, then check stock. If stock is greater than 200, give 15% discount; otherwise no discount.

Input:
Demand = 85
Stock = 40
User Type = premium
Festival = yes

Output:
Discount = 20%
===

d=int(input("Demand ="))
s=int(input("Stock ="))
u=input("Uesr Type =").lower()
f=input("Festival =").lower()

if d>=80:
    if s<50:
        if u=='premium':
            if f=='yes':
                print("Discount = 20%")
            else:
                print("Discount = 10%")
        else:
            print("Discount = No ")
    else:
        print("Discount = 5%")
elif d>=40 and d<=79:
    if f=='yes':
        print("Discount = 10%")
    else:
        print("Discount = No")
else:
    if s>=200:
        print("Discount = 15%")
    else:
        print("no discount")

=================================================================================9

9. Smart Loan Eligibility System

A bank approves loans based on salary, age, credit score, and EMI.

If salary is 40000 or above, then check age. If age is between 21 and 60, then check credit score. If credit score is 750 or above, then check EMI. If EMI is less than or equal to 40% of salary, approve at 8%; otherwise approve at 10%. If credit score is below 750, then check if it is at least 650. If yes, approve at 12%; otherwise reject.

If salary is below 40000, then check if salary is at least 25000 and credit score is at least 700. If yes, approve at 13%; otherwise reject.

Input:
Salary = 50000
Age = 30
Credit Score = 760
EMI = 18000

Output:
Loan Status = Approved at 8%
===

s=int(input("Salary ="))
a=int(input("Age ="))
c=int(input("Credit Score ="))
e=int(input("EMI ="))

if s>=40000:
    if 21<a and a<60:
        if c>=750:
            if e<=s*0.40:
                print("Loan Status = Approved at 8%")
            else:
                print("Loan Status = Approved at 10%")
        else:
            if c>=650:
                print("Loan status = Approved at 12%")
            else:
                print("Loan Status = Rejected")
else:
    if s>=25000:
        if c<=700:
            print("Loan Status = Approved at 13%")
        else:
            print("Reject")

=======================================================================================10

10. Military Recruitment Fitness System

Selection is based on age, BMI, running time, and medical condition.

If age is between 18 and 25, then check BMI. If BMI is between 18 and 25, then check running time. If running time is less than or equal to 15 minutes, then check medical. If medical is fit, select; otherwise medical reject. If running time is more than 15, physical fail. If BMI is not in range, BMI fail.

If age is between 26 and 30, then check running time and medical. If running time is less than or equal to 14 and medical is fit, conditional selection; otherwise reject.

If age is above 30 or below 18, not eligible.

Input:
Age = 23
BMI = 22
Running Time = 14
Medical = fit

Output:
Selection Status = Selected
===

a=int(input("Age ="))
b=int(input("BMI ="))
r=int(input("Running Time ="))
m=input("Medical =").lower()

if a>18 and a<25:
    if b>18 and b<25:
        if r<=15:
            if m=='fit':
                print("Selected")
            else:
                print("medical rejected")
        else:
            print("physical fail")
    else:
        print("BMI fail")
elif a>26 and a<30:
    if r<=14:
        if m=='fit':
            print("selection")
        else:
            print("reject")
else:
    if a>30 and a<18:
        print("not eligible")

'''












































        