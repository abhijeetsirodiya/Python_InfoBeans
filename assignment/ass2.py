'''Assignment 1: Time Converter
========================================

An event management company is developing a scheduling system. One of the key tasks is converting the duration of events from total seconds (which their sensor system records) into a more human-readable format of hours, minutes, and seconds.

Write a Python program that:
- Accepts the total event duration in seconds as input.
- Calculates how many hours, minutes, and seconds it corresponds to.
- Displays the output in the format:
  Hours: x, Minutes: y, Seconds: z

Sample Input:
Total event duration in seconds: 3672

Sample Output:
Hours: 1, Minutes: 1, Seconds: 12

'''
import math
z=int(input("Enter the total duration of event :"))

a=int(z/3600)

b=int((z/60))
c=(b-a*60)


d=(z-b*60)

print(f"Hours:{a},Minutes:{c},Second:{d}")

'''

Assignment 2: Lifetime Calculator
========================================

You are developing a feature for a health and wellness mobile app that helps users understand how long they've been alive in a more tangible way.

Write a Python program that:
- Accepts the user’s age in years as input.
- Calculates the approximate number of:
  Days lived (1 year = 365 days)
  Hours lived
  Minutes lived
- Displays the output in the format:

You've lived approximately:
Days: xxx
Hours: yyy
Minutes: zzz

Sample Input:
Enter your age in years: 18

Sample Output:
You've lived approximately:
Days: 6570
Hours: 157680
Minutes: 9460800


age=input("Enter your age :")
x=int(age)
a=(x*365)
print("You've lived approximately:")
print("Days:",a)
b=(a*24)
print("Hours:",b)
c=(b*60)
print("Minutes:",c)


===
Assignment 3: Split the Bill
========================================

You and your friends went out to eat. The bill was quite high and you want to split it evenly.

Write a Python program that:
- Accepts the total bill amount.
- Accepts the number of friends.
- Displays how much each person should pay.

Example:
Total bill = 1250
Friends = 5
Each should pay = 250.0


a=input("Enter the amount:")
b=input("Enter the number of friends:")
a=int(a)
b=int(b)
c=(a/b)
print("Total bill =",a)
print("Friends = ",b)
print("Each should pay =",c)

Assignment 4: Travel Fare Calculator
========================================

A cab company charges ₹15 per kilometer.

Write a Python program that:
- Accepts the number of kilometers traveled.
- Calculates the total fare.
- Displays the result.

Example:
Distance = 20 km
Total fare = ₹300


a=int(input("Enter the kilometers you traveled:"))
b=(a*15)
print(f"Distance = {a}km")
print("Total fare = ₹",b)


Assignment 5: Shopping Tax Calculator
========================================

Your shopping cart total doesn’t include tax. A 12% GST is applied.

Write a Python program that:
- Accepts the cart total amount.
- Calculates 12% tax.
- Displays the tax and final total amount.

Example:
Cart = ₹2000
Tax = ₹240
Total = ₹2240

total=int(input("Enter the cart total amount :"))
tax=(total*12/100)
a=(total+tax)
print("Cart = ₹",total)
print("Tax = ₹",tax)
print("Total = ₹",a)


===
Assignment 6: Smart Coin Machine
========================================

You insert an amount into a vending machine. It returns coins using the largest denominations possible (₹10 and ₹5).

Write a Python program that:
- Accepts the total amount.
- Calculates how many ₹10 coins and ₹5 coins will be dispensed.
- Displays the result.

Example:
Amount = ₹35
Output = ₹10 x 3, ₹5 x 1



amount=int(input("Enter the amount:"))
a=int(amount/10)
b=int(amount%10/5)
print(f" = ₹10 * {a}, ₹5 * {b}")


Assignment 7: Temperature Converter
========================================

A weather application needs to convert temperature from Celsius to Fahrenheit.

Write a Python program that:
- Accepts temperature in Celsius as input.
- Converts it to Fahrenheit using the formula:
  F = (C × 9/5) + 32
- Displays the result.

Example:
Celsius = 25
Fahrenheit = 77.0

C=int(input("Temprature in Celsius :"))
F = (C * 9/5) + 32
print("Celsius =",C)
print("Fahrenheit =",F)

Assignment 8: Simple Interest Calculator
========================================

A bank wants to help customers calculate the simple interest on their savings.

Write a Python program that:
- Accepts principal amount, rate of interest, and time (in years) as input.
- Calculates the simple interest using the formula:
  SI = (P × R × T) / 100
- Displays the simple interest.

Example:
Principal = 1000
Rate = 5
Time = 2
Simple Interest = 100.0

p=int(input("Enter the Principle:"))
print("Principle =",p)
r=int(input("Enter the rate:"))
print("rate =",r)
time=int(input("Enter the time in year:"))
print("Time =",time)
si=(p*r*time/100)
print("Simple Intrest =",si)

'''

























