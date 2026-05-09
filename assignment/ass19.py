'''
1. Utility Toolkit System

You are developing a Utility Toolkit Application for a small office. Employees use this tool to quickly perform common number operations like checking prime numbers, reversing numbers, etc.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Check Prime Number
2 → Check Palindrome Number
3 → Reverse a Number
4 → Count Digits
5 → Exit

Sample Run 1:
Input:
Enter your choice: 1
Enter number: 7

Output:
7 is a Prime Number

Sample Run 2:
Input:
Enter your choice: 2
Enter number: 121

Output:
121 is a Palindrome Number

Sample Run 3:
Input:
Enter your choice: 3
Enter number: 456

Output:
Reversed Number is: 654

Sample Run 4:
Input:
Enter your choice: 4
Enter number: 98765

Output:
Total digits: 5

Sample Run 5 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

Sample Run 6 (Exit):
Input:
Enter your choice: 5

Output:
Exiting program... Thank you!

Requirements:

* Use while loop to repeat menu
* Use match-case for decision making
* Handle negative numbers properly
* Use only loops and conditions
====

while True:
    print("\nMenu Option")
    print("1. Check Prime Number")
    print("2. Check palindrome Number")
    print("3. Reverse Number ")
    print("4. Count Number")
    print("5. Exit")
    choice=int(input("Enter Your Choice:"))
    match choice:
        case 1:
            n=int(input("Enter the number:"))
                
            if n<=1:
                print("Not a Prime Number")
            else:
                for i in range(2,n):
                    if n%i==0:
                        print("Not A Prime Number")
                        break
                else:
                    print("Prime Number")
        case 2:
            n=int(input("\nEnter The Number:"))
            s=0
            temp=n
            while n>0:
                a=n%10
                s=s*10+a
                n=n//10
                if temp==s:
                    print("The Number is pailndrom")
                    break
                else:
                    print("Not Pailndrom")
                    break

        case 3:
            n=int(input("Enter the Number :"))
            s=0
            while n>0:
                a=n%10
                s=s*10+a
                n=n//10
            print("Reverse Number is :",s)

        case 4:
            n=input("Enter the number:")
            count=0
            for i in n:
                count=count+1
            print("Total Number count is:",count)
        case 5:
            print(" Exit ")
            break
        case _:
            print("Invalid choice")

================================================================================2
2. Employee Salary Processor
Scenario:
You are developing an Employee Salary Processing System for a company’s HR department. The system is used to manage and calculate employee salary details such as allowances, tax deductions, and final payable salary.

The HR staff may not always follow the correct sequence while using the system. For example, they might try to calculate net salary or tax before entering the basic salary. Your program must handle such situations properly.

👉 Important Condition:
If the Basic Salary is not entered, the system should display:
"Please enter basic salary first"
and should not perform any further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Basic Salary
2 → Calculate HRA (20%) and DA (10%)
3 → Calculate Net Salary
4 → Tax Deduction

* Salary > 50000 → 10% tax
* Otherwise → 5% tax
  5 → Display Salary Slip
  6 → Exit

---

Sample Run 1:
Input:
Enter your choice: 3

Output:
Please enter basic salary first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter Basic Salary: 40000

Output:
Basic Salary recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
HRA: 8000
DA: 4000

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Net Salary (before tax): 52000

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
Tax Deduction: 5200

---

Sample Run 6:
Input:
Enter your choice: 5

Output:
----- Salary Slip -----
Basic Salary: 40000
HRA: 8000
DA: 4000
Net Salary: 52000
Tax: 5200
Final Salary: 46800

---

Sample Run 7 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 8 (Exit):
Input:
Enter your choice: 6

Output:
Exiting program... Thank you!


salary=None
hra=da=tax=netsalary=0
while True:
    print("\tMenu Option")
    print("1. Enter Basic Salary")
    print("2. Calculate HRA (20%) and DA (10%)")
    print("3. Calculate Net Salary")
    print("4. Tax Deducation")
    print("5. Display Salary Slip")
    print("6. Exit")
    choice=int(input("Enter Your Choice:"))
    match choice:
        case 1:
            salary=int(input("Enter Basic Salary :"))
            print("Basic Salary recorded successfully")
        case 2:
            if salary==None:
                print("please enter basic salary first")
            else:
                hra=salary*0.2
                da=salary*0.1
                print("HRA:",hra)
                print("DA:",da)
        case 3:
            if salary==None:
                print("Please enter basic salary first")
            else: 
                netsalary=(salary+hra+da)
                print("Net Salary (before tax):",netsalary)
        case 4:
            if salary==None:
                print("please enter basic salary first")
            else:
                if netsalary>50000:
                    tax=netsalary*0.10
                    print("Tax Deduction:",tax)
                else:
                    print(netsalary)
                    tax=netsalary*0.05
                    print("Tax Deduction:",tax)
 
        case 5:
            print("----Salary Slip----")
            print("Basic salary:",salary)
            print("HRA:",hra)
            print("DA:",da)
            print("Net Salary:",netsalary) 
            print("Tax:",tax)
            final=netsalary-tax
            print("Final Salary:",final)
        case 6:
            print("Exit program Thank you..")
            break
        case _:
            print("Invalid choice")
            

===========================================================================3

3.


 Smart Banking System

Scenario:
You are developing a Smart Banking System for a bank to help customers perform basic banking operations such as deposit, withdrawal, balance checking, and interest calculation.

Sometimes, users may try to withdraw money or check balance before depositing any amount. Your system must handle such situations properly.

👉 Important Condition:
If no amount has been deposited yet, the system should display:
"No balance available. Please deposit first"
and should not allow withdrawal, balance check, or interest calculation.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Deposit Money
2 → Withdraw Money
3 → Check Balance
4 → Apply Interest

* Balance > 50000 → 5% interest
* Otherwise → 3% interest
  5 → Exit

---

Sample Run 1:
Input:
Enter your choice: 2

Output:
No balance available. Please deposit first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter amount to deposit: 10000

Output:
Amount deposited successfully

---

Sample Run 3:
Input:
Enter your choice: 3

Output:
Current Balance: 10000

---

Sample Run 4:
Input:
Enter your choice: 2
Enter amount to withdraw: 15000

Output:
Insufficient balance

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
Interest added: 300
Updated Balance: 10300

---

Sample Run 6:
Input:
Enter your choice: 2
Enter amount to withdraw: 5000

Output:
Withdrawal successful

---

Sample Run 7 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 8 (Exit):
Input:
Enter your choice: 5

Output:
Exiting system... Thank you!
====

while True:
    print("\nMenu Option:")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Apply Interest")
    print("5. Exit")
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            amount=int(input("Enter amount to deposit:"))
            print("Amount deposite successfully")
        case 2:
            withdraw=int(input("Enter amount to withdraw:"))
            if withdraw > amount:
                print("No balance available. please deposite first")
            else:
                current=(amount-withdraw)
                print("Amount withdraw successfully")
        case 3:
            print("Current Balance:",current)
        
        case 4:
            if amount<=0:
                print("No balance available. please deposite first")
            else:
                if amount > 50000:
                    intrest=(amount*0.05)
                    print("Intrest added:",interst)
                    print("Update Balance:",amount+intrest)
                else:
                    intrest=(amount*0.03)
                    print("Intrest added:",intrest)
                    print("Update Balance:",amount+intrest)
        
        case 5:
            print("Exiting system ... Thank you!!")
            break
        case _:
            print("Invilid choice. Plese try again")

==============================================================================4

4. Electricity Bill Management System

You are developing an Electricity Bill Management System for a power distribution company. The system helps calculate electricity bills for customers based on their unit consumption.

Sometimes, the operator may try to calculate the bill or apply surcharge before entering the number of units consumed. Your system must handle such situations properly.

👉 Important Condition:
If units are not entered, the system should display:
"Please enter units consumed first"
and should not perform further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Units Consumed
2 → Calculate Bill Amount

* First 100 units → ₹5 per unit
* Next 100 units → ₹7 per unit
* Above 200 units → ₹10 per unit
  3 → Apply Surcharge
* If bill > 2000 → 10% surcharge
* Otherwise → 5% surcharge
  4 → Display Final Bill
  5 → Exit

---

Sample Run 1:
Input:
Enter your choice: 2

Output:
Please enter units consumed first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter units consumed: 250

Output:
Units recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
Bill Amount: 1700

(Explanation: 100×5 = 500, 100×7 = 700, 50×10 = 500 → Total = 1700)

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Surcharge: 85

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
----- Final Bill -----
Units: 250
Bill Amount: 1700
Surcharge: 85
Total Payable: 1785

---

Sample Run 6 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 7 (Exit):
Input:
Enter your choice: 5

Output:
Exiting system... Thank you!
                            
======
'''
unit=None
while True:
    print("\nMenu Options:")
    print("1. Enter Units Consumed")
    print("2. Calculate Bill Amount")
    print("3. Apply Surcharge")
    print("4. Display Final Bill")
    print("5. Exit")
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            unit=int(input("Enter units consumed:"))
            print("Unit recorded successfully")
        case 2: 
            if unit<=0:
                print("Please enter units consumed first")
            else:
                if unit>200:
                    bill= (unit * 5) if unit <= 100 else (100 * 5 + (unit - 100) * 7) if unit <= 200 else (100 * 5 + 100 * 7 + (unit - 200) * 10)
                    print("Bill amount:",bill)
                else:
                    bill= unit*5
                    print("Bill amount:",bill)
        case 3:
            if unit==None:
                print("Plese enter units consumed first")
            else:
                if bill > 2000:
                    surcharge=bill*0.1
                    print("Surcharge:",surcharge)
                else:
                    surcharge=bill*0.05
                    print("Surcharge:",surcharge)
        case 4:
            print("Units:",unit)
            print("Bill Amount:",bill)
            print("Surcharge:",surcharge)
            print("Total payable:",bill+surcharge)
        case 5:
            print("Exiting system... Thank you!")
            break
        case _:
            print("Invalid choice")



































































