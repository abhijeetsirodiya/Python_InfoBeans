'''
1. Insurance Claim Approval System

An insurance company processes claims based on policy age, claim amount, and accident type. The approval depends on multiple levels of verification to reduce fraud.

If the policy age is at least 2 years, then check the claim amount. If the claim amount is up to 50000, then check the accident type. If it is minor, approve the claim; otherwise, approve it with inspection. If the claim amount is between 50001 and 200000, then check the accident type. If it is major, approve with investigation; otherwise reject. If the claim amount exceeds 200000, reject. If the policy age is less than 2 years, then check accident type. If minor, reject; otherwise mark as pending review.

Input:
Policy Age = 3
Claim Amount = 120000
Accident Type = major
=======

p=int(input("Policy Age ="))
ca=int(input("Calm Amount ="))
at=input("Accident Type =").lower()

if p>=2:
    if ca<=50000:
        if at=='minor':
            print("approve the clam")
        else:
            print("approve it with inspection")
    elif ca>=50001 and ca<=200000:
        if at=='major':
            print("Approve with investigation")
        else:
            print("Reject")
    elif ca>=200000:
        print("Reject")
else:
    if p<2:
        if at=='minor':
            print("Reject")
        else:
            print("Pending")
================================================2
2. University Admission System

A university decides admission based on marks, entrance score, and category of the student.

If marks are 70 or above, then check entrance score. If entrance score is 80 or above, then check category. If general, admit; otherwise admit with scholarship. If entrance score is less than 80, then check if marks are 85 or above. If yes, admit under management quota; otherwise reject. If marks are below 70, then check if category is not general and marks are at least 60. If yes, check entrance score. If it is 70 or above, waitlist; otherwise reject. If none of these conditions match, reject.

Input:
Marks = 72
Entrance Score = 85
Category = general

Output:
Admission Status = Admitted

m=int(input("Marks ="))
es=int(input("Enterance Score ="))
c=input("Catagory =")

if m>=70:
    if es>=80:
        if c=='general':
            print("Admited")
        else:
            print("admit with schlorship")
    else:
        if es<80:
            if m>=85:
                print("admit under management quata")
            else:
                print("reject")
        elif m<70 and m>=60:
            if c!='general':
                if es>=70:
                    print("waitlist")
                else:
                    print("reject")
else:
    print("reject")

============================================================3

3. Smart Loan Risk Categorization

A bank categorizes loan applicants into risk levels based on salary, credit score, and number of existing loans.

If salary is at least 30000, then check credit score. If credit score is 750 or above, then check number of loans. If zero, assign low risk. If loans are up to 2, assign medium risk; otherwise high risk. If credit score is below 750, then check if salary is at least 50000. If yes, check if credit score is at least 650. If yes, medium risk; otherwise high risk. If salary is less than 30000, mark as not eligible.

Input:
Salary = 40000
Credit Score = 760
Existing Loans = 1

Output:
Risk Level = Medium Risk
===

s=int(input("Salary ="))
cs=int(input("Credit Score ="))
el=int(input("Existing Loans ="))

if s>=30000:
    if cs>=750:
        if el==0:
            print("low risk")
        elif el<=0 or el<=2:
            print("medium risk")
        elif el>2:
            print("high risk")
    elif cs<750 :
        if s>50000:
            if cs<650:
                print("medium risk")
else: 
    print("not eligible")

=============================================================4
4. E-Learning Course Access System

An online learning platform grants access based on subscription type, course progress, and test score.

If subscription is premium, then check progress. If progress is at least 80, then check test score. If score is at least 70, unlock certificate; otherwise allow retry. If progress is less than 80, ask to complete course. If subscription is basic, then check progress. If progress is at least 50, allow limited access; otherwise lock content. If subscription is neither, deny access.

Input:
Subscription = premium
Progress = 85
Test Score = 65

Output:
Access Status = Retry Test
===

s=input("Subscription =").lower()
p=int(input("progress ="))
t=int(input("Test Score ="))

if s=='premium':
    if p>=80:
        if t>=70:
            print("Access Status =unlock certificate")
        else:
            print("Access Status =retry Test")
    
    else:
        print("Access Status =complete cource")
elif s=='basic':
        if p<=50:
            print("Access Status =limited access")
        else:
            print("Access Status =lock content")
else:
    if s=='neither':

        print("Access Status =deny access")
====================================================================5

5. Smart Warehouse Dispatch System

A warehouse decides dispatch strategy based on stock availability, priority level, and delivery distance.

If stock is at least 100, then check priority. If high priority, then check distance. If distance is up to 200, dispatch immediately; otherwise use fast courier. If priority is not high, then check if stock is at least 300. If yes, bulk dispatch; otherwise normal dispatch. If stock is less than 100, then check if stock is at least 50. If yes, and priority is high, partially dispatch; otherwise hold. If stock is below 50, mark out of stock.

Input:
Stock = 120
Priority = high
Distance = 300

Output:
Dispatch Status = Dispatch via Fast Courier
===

s=int(input("Stock="))
p=input("Priority =").lower()
d=int(input("Distance ="))

if s>=100:
    if p=='high':
        if d>=200:
            print("Dispatch immeditely")
        else:
            print("use fast courier")
    elif p=='not high':
        if s<=300:
            print("bulk dispatch")
        else:
            print("normal dispatch")
else:
    if s<=50:
        if p=='high':
            print("partially dispatch")
        else:
            print("hold")
    else:
        print("out of stock")

================================================6

6. Banking Fraud Detection System

A bank monitors transactions based on amount, location, OTP verification, and account age.

If transaction amount is at least 10000, then check location. If international, then check OTP verification. If verified, allow; otherwise block. If location is domestic, then check if amount is at least 50000. If yes, check account age. If account age is at least 2 years, allow; otherwise flag. If amount is less than 50000, allow. If transaction amount is less than 10000, then check unusual activity. If yes, flag; otherwise allow.

Input:
Transaction Amount = 60000
Location = domestic
Account Age = 1

Output:
Transaction Status = Flagged

a=int(input("Transaction Amount ="))
l=input("Location =").lower()
ac=int(input("Account Age ="))
o=input("OTP status =")

if a>=10000:
    if l=='internationl':
        if o=='verified':
            print("allow")
        else:
            print("block")
    elif l=='domastic':
        if a>=50000:
            if ac>=2:
                print("allow ")
            else:
                print("flag")
else:
    if t<=10000:
        print("flag")
    else:
        print("allow")

===================================================================7
           

7. Ride Booking Surge Pricing System

A ride booking app calculates fare multiplier based on demand, time, and distance.

If demand is at least 80, then check time. If peak time, then check distance. If distance is at least 10, apply 2x fare; otherwise 1.5x. If not peak time, then check if demand is at least 90. If yes, 1.8x; otherwise 1.3x. If demand is less than 80, then check if demand is at least 50. If yes, then if peak time, apply 1.2x; otherwise normal fare. If demand is below 50, normal fare.

Input:
Demand = 85
Time = peak
Distance = 12

Output:
Fare Multiplier = 2x Fare
===

d=int(input("Demand ="))
t=input("Time =")
distance=int(input("Distance ="))

if d>=80:
    if t=='peak':
        if distance>=10:
            print("2x Fare")
        else:
            print("1.5x")
    else:
        if d>=90:
            print("1.8")
        else:
            print("1.3")
else:
    if d>=50:
        if t=='peak':
            print("1.2x")             
        else:
            print("normal fare")
    else:
        if d<=50:
            print("normal fare")

====================================================================8

8. Smart Farming Irrigation System

A farming system decides irrigation based on soil moisture, temperature, crop type, and rainfall prediction.

If soil moisture is 30 or below, then check temperature. If temperature is at least 35, then check crop type. If wheat, high water supply; otherwise moderate supply. If temperature is less than 35, moderate supply. If moisture is above 30, then check if it is up to 60. If yes, then check rainfall. If rain expected, delay irrigation; otherwise light irrigation. If moisture is above 60, no irrigation.

Input:
Soil Moisture = 25
Temperature = 36
Crop = wheat

Output:
Irrigation = High Water Supply

s=int(input("Soil Moisture ="))
t=int(input("Temperature ="))
c=input("Crop =").lower()
r=input("rainfall expected or not =").lower()                                         

if s<=30:
    if t>=35:
        if c=='wheat':
            print("high water supply")
        else:
            print("moderate supply")
    else:
        print("moderate supply")
else:
    if t<=60:
        if r=='expected':
            print("delay irrigation")
        else:
            print("light irrigation")
    else:
        print("no irragition")
  
===============================================================9

9. Multi-Level Employee Promotion System

A company promotes employees based on experience, rating, projects completed, and salary.

If experience is at least 5 years, then check rating. If rating is at least 4, then check projects. If projects are at least 3, then check salary. If salary is up to 50000, promote with 30 percent hike; otherwise 20 percent hike. If projects are less than 3, promote with 10 percent hike. If rating is below 4, no promotion. If experience is less than 5, then check if rating is 5. If yes, fast track promotion; otherwise no promotion.

Input:
Experience = 6
Rating = 4
Projects = 2

Output:
Promotion Status = Promoted with 10% hike
===

e=int(input("Experience ="))
r=int(input("Rating ="))
p=int(input("Projecting ="))
s=int(input("salary ="))

if e>=5:
    if r>=4:
        if p>=3:
            if salary<=50000:
                print("Promotion Status = 30 percent hike")
            else:
                print("Promotion Status = 20 percent hike")
        else:
            print("Promotion Status =  10 percent hike")
    else:
        print("Promotion Status = no promotion")
else:
    if r==5:
        print("Promotion Status = fast track promotion")
    else:
        print("Promotion Status = no promtion")

=========================================================================10

10. Smart Restaurant Order Processing System

A restaurant offers discounts and benefits based on order amount, customer type, and payment method.

If order amount is at least 2000, then check customer type. If VIP, then check payment method. If online, give free dessert and 20 percent discount; otherwise only free dessert. If not VIP, then check if amount is at least 5000. If yes, give 15 percent discount; otherwise 10 percent discount. If order amount is less than 2000, then check if it is at least 1000. If yes, then if customer is VIP, give 10 percent discount; otherwise 5 percent discount. If below 1000, no offer.

Input:
Order Amount = 2500
Customer Type = VIP
Payment Method = online

Output:
Offer = Free Dessert + 20% Discount
===

o=int(input("Order Amount ="))
c=input("Customer type =").lower()
p=input("Payment Method =").lower()

if o>=2000:
    if c=='vip':
        if p=='online':
            print("Offer = Free Dessert and 20% discount")
        else:
            print("Offer = only free dessert")
    else:
        if o>=5000:
            print("Offer = 15% discount")
        else:
            print("Offer = 10% discount")
else:
    if o>=1000:
        if c=='vip':
            print("Offer = 10% discount")
        else:
            print("Offer = 5% discount")

'''



































           
             