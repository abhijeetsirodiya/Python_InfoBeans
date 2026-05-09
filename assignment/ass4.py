'''
Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75

#sol

a=int(input("Total bill amount ="))
g=int(input("GST ="))
sc=int(input("Service charge ="))
f=int(input("Number of friends ="))

x=((a*5)/100)
y=((a*10)/100)
z=(a+x+y)
p=(z/f)

print("Final Bill =",z)
print("Each Person Pays =",p)


Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0
#sol

mp=int(input("Mobile price ="))
dp=int(input("Down payment ="))
ir=int(input("Intrest rate ="))
m=int(input("Months ="))

print("Remaining Amount =",mp-dp)
intrest=((mp*10)/100)
t=(mp+intrest)
print("Total with intrest =",t)
mi=(t/12)
print("Monthly EMI =",mi)


Assignment 3: Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2
#sol

m1,m2,m3,m4,m5=map(int,input("Marks =").split())
total=(m1+m2+m3+m4+m5)
print("Total =",total)
avg=(total/5)
print("Average =",avg)
p=((total/500)*100)
print("Percentage =",p)
=====================================================
Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km
#sol

s=int(input("Speed ="))
h,m=map(int,input("Time =").split())
t1=((h*60)+m)
total=float(t1/60)
print(F"Total time ={total} hours")
d=int(total*s)
print(f"Distance ={d}km")

==============================================================5

Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5
#sol

ms=int(input("Monthly salary ="))
wd=int(input("Working day ="))
wh=int(input("Working hours per day ="))
sd=(ms/wd)
print("Salary per day =",sd)
sh=(sd/wh)
print("Salary per hour =",sh)

=============================================================6

Assignment 6: Data Storage Conversion

A user wants to convert data from GB into MB and KB.

Input:
Data = 5 GB

Expected Output:
In MB = 5120.0
In KB = 5242880.0

#sol

data=int(input("Data in GB ="))
mb=float(data*1024)
print("In MB =",mb)
kb=float(mb*1024)
print("In KB =",kb)

===============================================================7
Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3
                                                
Expected Output:
Total Balls = 291
Run Rate = 5.67

#sol
'''
import math
t=int(input("Total run ="))
o=float(input("Overs ="))
x=int(o)
a=int((o*10)%10)
b=(x*6)
c=(a+b)
print("Total Balls =",c)

r=(t/o)
print("Run Rate ",round(r,2))
'''
=======================================================8



Assignment 8: Compound Interest

A person invests money in a bank that provides compound interest annually.

Input:
Principal = 10000
Rate = 5%
Time = 2 years

Expected Output:
Amount after interest = 11025.0

p=int(input("Principal ="))
r=int(input("Rate ="))
t=int(input("Time ="))

i=(p*(1+r/100)**t)
print("Amount after intrest = ",i)

===================================================9
Assignment 9: Petrol Cost Calculation

You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

Input:
Distance = 450 km
Mileage = 15 km/litre
Petrol price = 110/litre

Expected Output:
Petrol Used = 30.0 litres
Total Cost = 3300.0

d=int(input("Distance ="))
m=int(input("Mileage ="))
p=int(input("Petrol price ="))

a=(d/m)
print(f"Petrol Used = {a} litres")

c=(a*p)
print(f"Total Cost = {c} litres")

====================================================10
Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4

t=int(input("Total seconds ="))

h=((t//60)//60)
m=((t//60)%60)
s=(t%60)
print("Hours =",h)
print("minutes =",m)
print("second =",s)

===================================================11

Assignment 11: Expression Evaluation

A billing system applies nested calculations with discounts and extra charges using brackets and unary operators.

Input:x=(50 + (10 * (+(2**3))) / 4 - (-6 % 4))
print(x)




================================================12



Assignment 12: Expression Evaluation

A gaming score system calculates bonus points using exponent and applies penalties using unary negative values and brackets.

Input:

x= 100 - (20 * (3**2)) + (40 / (+5)) - (-3)
print(x)


================================================13




Assignment 13: Expression Evaluation

A shopping application applies offers using exponent and grouped calculations with unary adjustments.

Input:
x=25 + (5 * (6**2) // 3) - (-(8 % 5)) + (+2)
print(x)


=================================================14



Assignment 14: Expression Evaluation

A travel fare calculator computes total fare using grouped operations, power calculations, and unary adjustments.

Input:
x=(80 / (4 * 2)) * (+(2**2)) + 15 - (-(9 % 2))
print(x)





===================================================15


Assignment 15: Expression Evaluation

An electricity billing system uses nested brackets, exponent-based scaling, and unary corrections.

Input:
x=60 + (12 * (2**3) // (+(4))) - (-(10 % 3))
print(x)


=====================================================16

Assignment 16: Expression Evaluation

A performance evaluation system calculates final score using grouped operations, exponent, division, and unary adjustments.

Input:
x=45 + (15 * (2**2)) - (20 / (+(5))) + (-(7 % 3))
print(x)


'''




















