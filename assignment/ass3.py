'''Assignment 1: Speed Calculator

Write a Python program that:

Accepts distance (in km) and time (in hours).
Calculates speed.

Input:
Distance = 120
Time = 2

Output:
Speed = 60 km/h
====
d=int(input("Distance ="))
t=int(input("Time ="))
s=d/t

print(f"Speed = {s}km/h")
===========================================================2

Assignment 2: Salary Calculator

Write a Python program that:

Accepts daily wage and number of days.
Calculates total salary.

Input:
Daily wage = 500
Days = 26

Output:
Salary = 13000
======


d=int(input("Daily wage ="))
day=int(input("Days ="))

s=d*day
print("Salary =",s)

=========================================================3

Assignment 3: Electricity Bill Calculator

Write a Python program that:

Accepts number of units.
Calculates bill (₹6 per unit).

Input:
Units = 100

Output:
Bill = 600

====

u=int(input("Units ="))
b=u*6
print("Bill =",b)

===========================================================4
Assignment 4: Area of Rectangle

Write a Python program that:

Accepts length and breadth.
Calculates area.

Input:
Length = 10
Breadth = 5

Output:
Area = 50
=====

l=int(input("Length ="))
b=int(input("Breadth ="))
a=l*b
print("Area =",a)

=============================================================5
Assignment 5: Average Marks Calculator

Write a Python program that:

Accepts marks of 3 subjects.
Calculates average.

Input:
Marks = 80, 90, 70

Output:
Average = 80.0
=====

m1,m2,m3=map(int,input("Marks =").split(","))
a=(m1+m2+m3)/3
print("Average =",a)
=============================================================6

Assignment 6: Discount Calculator

Write a Python program that:

Accepts total amount.
Calculates 10% discount and final price.

Input:
Amount = 1000

Output:
Discount = 100
Final = 900

===

total=int(input("Amount ="))
discount=((total*10)/100)
final=(total-discount)
print("Discount =",discount)
print("Final =",final)
===========================================================7

Assignment 7: Circle Area Calculator

Write a Python program that:

Accepts radius.
Calculates area of circle.

Input:
Radius = 7

Output:
Area = 153.86
===

r=int(input("Radius ="))
a=(3.14*r*r)
print("Area =",a)
=====================================================8


Assignment 8: Data Storage Converter

Write a Python program that:

Accepts value in MB.
Converts into GB.

Input:
MB = 2048

Output:
GB = 2.0

====

m=int(input("MB ="))
gb=(m/1024)
print("GB =",gb)

=====================================================9
Assignment 9: Fuel Cost Calculator

Write a Python program that:

Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.

Input:
Distance = 100
Mileage = 20
Petrol Price = 100

Output:
Cost = 500
====


d=int(input("Distance ="))
m=int(input("Milege ="))
p=int(input("Petrol Price ="))

c=((d/m)*p)
print("Cost =",c)
============================================================10


Assignment 10: Percentage Calculator

Write a Python program that:

Accepts total marks and obtained marks.
Calculates percentage.

Input:
Total = 500
Obtained = 400

Output:
Percentage = 80%
====


t=int(input("Total ="))
o=int(input("Obtained ="))
p=(o/t*100)
print(f"Percentage ={p}%")

=========================================================11

Assignment 11: Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2
Seconds = 30

Output:
Total Seconds = 3750
====
a=int(input("Hours ="))
b=int(input("Minutes ="))
c=int(input("Second ="))

h=int(a*60*60)
m=int(b*60)

t=(h+m+c)
print("Total Secands =",t)
==========================================================12
Assignment 12: Change Return System

Write a Python program that:

Accepts amount.
Calculates ₹100, ₹50, ₹10 notes.

Input:
Amount = 380

Output:
₹100 x 3
₹50 x 1
₹10 x 3
=========

a=int(input("Amount ="))

s=int(a/100)
f=int((a%100)/50)
t=int(((a%100)%50)/10)
print(f"₹100 * {s}")
print(f"₹50  * {f}")
print(f"₹10  * {t}")

==========================================================13

Assignment 13: Compound Interest Calculator

Write a Python program that:

Accepts principal, rate, and time.
Calculates compound interest.

Input:
Principal = 1000
Rate = 10
Time = 2

Output:
Amount = 1210.0
Compound Interest = 210.0
====

p=int(input("Principal ="))
r=int(input("Rate ="))
t=int(input("Time ="))
c=p*(1+r/100)**t-p
print("Amount =",p+c)
print("Compound Interest =",c)

============================================================14
Assignment 14: Simple Profit or Loss Calculator

Write a Python program that:

Accepts cost price and selling price.
Calculates profit/loss and percentage.

Input:
Cost Price = 1000
Selling Price = 1200

Output:
Profit = 200
Profit % = 20.0
=====

cp=int(input("Cost Price ="))
sp=int(input("Selling Price ="))

profit=int((sp-cp))
p=(profit/cp*100)

print("\nprofit =",profit)
print("Profit % =",p)

loss=int(cp-sp)
l=((loss/cp)*100)
print("\nloss % =",loss)
print("loss % =",l)

=============================================================15
Assignment 15: Average Speed for Multiple Trips

Write a Python program that:

Accepts distance1, time1, distance2, time2.
Calculates average speed.

Input:
Distance1 = 60
Time1 = 1
Distance2 = 40
Time2 = 1

Output:
Average Speed = 50 km/h
=====

d1=int(input("Distance1 ="))
t1=int(input("Time1 ="))
d2=int(input("Distance2 ="))
t2=int(input("Time2 ="))
a=((d1+d2)/(t1+t2))

print(f"Average Speed = {a}"km/h)

'''
d=int(input("Distance ="))
m=int(input("Mileage ="))
p=int(input("Petrol price ="))

a=((d/m)*p)
print("Cost =",a)























