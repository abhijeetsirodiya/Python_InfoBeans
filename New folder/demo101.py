
'''
marks1,marks2=input("enter both marks").split()
print(marks1)
print(marks2)
marks1=int(marks1)
marks2=int(marks2)
print(marks1+5)
print(marks2+10


import keyword
print(keyword.kwlist)

import keyword
print(len(keyword.kwlist))

import keyword
print(keyword.iskeyword("if"))	



multipal values
a=10
print(a)
a="abhijeet"
print(a)
a=15.65
print(a)

a=10
print(type(a))
a="abhijeet"
print(type(a))
a=15.65
print(type(a))

				
a,b,c,d=1,2,3,4

print(a)

print(b)

print(c)

print(d)


SWAPPING

a=10
b=20
a,b=b,a
print(a)

print(b)



a=10
b=20
abhi=a
a=b
b=abhi

print(a)
print(b)


output 


print("abhijeet")
print(10)
print(12.43)
print("true")




name="abhijeet"
age=21
print(name,age)


name="abhijeet"
age=21
print(name,age,sep="->")



name="abhijeet"
age=21
print(name,age,sep=",")


name="abhijeet"
age=21
print(name,age,sep="\n")

End in python

print("abhijeet")
print("sirodiya")


print("abhijeet",end=" ")
print("sirodiya")


print("abhijeet \n sirodiya")


print("abhijeet \t sirodiya")


name="abhijeet"
print("name of the person is:",name)

name ="abhijeet"
print("name of the person is {name}")

name ="abhijeet"
print(f"name of the person is {name}")


name="abhijeet"
age=21
print(f"next year age of {name} {age+1}")


name="abhijeet"
print(f"hello {name + " how are you !!"}" )

name="abhijeet"
age=21
print(f"hello {name} welcome your age is {age}")

name="abhijeet"
age=21
address="indore"
print(f"hello {name} welcome your age is {age} and your address is {address}")

ERROR----


name="abhijeet"
age=21
print("your address is {address})

name="abhijeet"
age=21
print(f" address is {})


3RD methord USING FORMAT

name="abhijeet"
age=21
print("age is {} ".format(age))

name="abhijeet"
age=21
address="indore"
print("name is {} age is {} address is {}".format(name,age,address))


Input function--------------

name=input("Enter the name :")
print("your name is ",name)

a=input("Enter the first number :")
b=input("Enter the second number :")
print("your sum is :",a+b)


a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
print("your sum is :",a+b)


salary1=int(input("Enter the first person salary :"))
salary2=int(input("Enter the second person salary :"))
print("the sum of your salary is :",(salary1+salary2))



TAKING MULTIPLE INPUTS IN ONE LINE ---------


name,address=input("enter the name and address ").split()
print("name is",name)
print("address is ",address)


name,address = input("enter the name and address ").split(" , ")
print("name is",name)
print("address is ",address)

id,name,address = input("enter the id  name and address ").split(maxsplit=2)
print("id is",id)
print("name is",name)
print("address is ",address)


name,age= input("Enter the name and age :").split()


print("name is :",name)
print("age is :",age)

age=int(age)
print("next year age will be ",age+1)


marks1,marks2=input("Enter the both marks:").split()
print(marks1)
print(marks2)
marks1=int(marks1)
marks2=int(marks2)
print(marks1+5)
print(marks2+10)


MAP FUNCTION USE FOR  


marks1,marks2=map(input("enter both")).split()
print(marks1)
print(marks2)
print(marks1+5)
print(marks2+10)



data=input("Enter the both no.:").split()
print(data)
print(data[0])



m1,m2=int(input("Enter the both no.:").split())
print(m1)
print(m2)

m1,m2=map(float,input("Enter the both no.:").split())
print(m1)
print(m2)



print("===Resume===")
name="Alice Johnson"
Email="alice@example.com"
Exprience="2 years at XYZ Ltd."

print("Name        :",name)
print("Email       :",Email)
print("Skills 	   : -Java "
		    "\n\t -HTML &CSS"
		    "\n\t -PROBLEM SOLVING")
print("Exprience   :",Exprience)

=====================================
INTEGER DATA TYPE
=====================================
a=10
b=-10
c=99999
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

a=10
b=-10
c=99999_9999999_9999
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))


binary to Decimal
=================

a=0b1011
print(a)

a=0b1100
print(a)

a=0B1101
print(a)

b=-0B1110
print(b)

octal to decimal
=================

b=0O157
print(b)
print(type(b))

b=0o155
print(b)
print(type(b))

b=-0O156
print(b)
print(type(b))


Hexadecimal to decimal 0to 9 and A to F
======================

a=0xABC
print(a)
print(type(a))

b=0xA
print(b)
print(type(b))

b=0xE
print(b)
print(type(b))

b=0xf
print(b)
print(type(b))

b=0xdeep          ======ERROR
print(b)
print(type(b))


=================
CONVERTION BINARY , DECIMAL , OCTAL , HEXADECIMAL
====================

print(bin(0o10))===========decimal to binary==

print(bin(0o127))========octal to binary

print(oct(15))=============decimal to octal

print(oct(0b111))==========binary to octal

print(hex(15))========================decimal to hexadicmal

============================
FLOAT DATA TYPE                NOTE-there is no double in python
==========================

a=15.155
b=14.4545
c=0.0055
print(a)
print(c)
print(c)

print(type(a))
print(type(c))
print(type(c))

x=9999999_99999999_2222222
print(x)
print(type(x))

NOTE- binary,octal,hexa not work in float


x=0x157
print(x)
print(type(x))


x=5/2    ====float
print(x)
print(type(x))

x=5//2   ====int only
print(x)
print(type(x))


import math
a=3.7
print(math.ceil(a))============nearest up value

a=3.2
print(math.floor(a))==========nearest down value

b=-4.3
print(abs(b))============positive kar deta hai

c=4.555963
print(round(c,2))============2 hai toh decimal ke baad 2 value lega

c=4.555963
print(round(c,3))============3 hai toh decimal ke baad 3 value lega

=================
REPRESENTING FLOAT IN DIFFERENT WAY
=================

import math
a=1.2e2                       ======2e2 is equal to  2*10*10
print(a)
print(type(a))

a=1.2e3                       =====2e3 is  2*10*10*10

print(a)
print(type(a))


COMPLEX NUMBER 

ex=1

a=3+4j
print(a)
print(type(a))

ex=2

x=3+4j
y=-1+2j
z=12.5
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))


ex=3

x=4j
print(x)
print(type(x))


ex=4

x=3+4j
print(x.real)
print(x.imag)

x=complex(input("enter the complex number:"))
print(x.real)
print(x.imag)

ERROR

x=3+4i

print(x.real)
print(x.imag)

ex=5

x=0b1111+4j
print(x)
print(type(x))

NOTE:- IN CASE OF IMAGENARY OTHER BASE IS NOT ALLOWED
ERROR
X=0B1010+0B1111j
print(x)
print(type(x))

EX=6
ADD , SUB , MULTI , DIV CAN BE DONE IN PYTHON

x=3+6j
y=5+9j
print(x+y)

x=3+6j
y=5+9j
print(x-y)

x=3+6j
y=5+9j
print(x*y)

x=3+6j
y=5+9j
print(x/y)

BOOLEAN DATA TYPE
EX=1

x=True
print(x)
print(type(x))

ERROR
x=true
print(x)
print(type(x))

ex=2

print(True+True)
print(True+False)
print(False+False)

print(True+True)
print(True+False)
print(False+False)
print(True*10)

ex=4

x='True'
print(x)
print(type(x))

NOTE:- PYTHON DOSNOT HAVE A FIX TYPE LIKE C & C++ . HEAR SIZE OF DATA TYPE IS DAYNIMIC . IT DEPENDS ON THE VALUDE STORE , THE SAYSTEM 


PYTHON IMPLIMANTATION


import sys
a=10958955224655656999999999999999
b=10.5
c=True
d=""
e=None
f="deepika"
print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
print(sys.getsizeof(d))
print(sys.getsizeof(e))
print(sys.getsizeof(f))

print(type(d))
print(type(e))
print(type(f))

ex=2
objext change hoga kyuki string ki value add ho gai
import sys
a="A"
b="a"*100
print(sys.getsizeof(a))
print(sys.getsizeof(b))

#same object rahega ==
x=10
y=10
z=10
print(id(x))
print(id(y))
print(id(z))

#ALL FUNDAMENTAL DATA TYPE ARE INMUTABLE 
# INT , FLOAT , BOOL , COMPLEX & STR
x=True
y=True
z='True'
print(id(x))
print(id(y))
print(id(z))

x=10
print(id(x))
x=x*5
print(id(x))

str="deepika"
print(id(str))
str=str+"jii"
print(id(str))

#TYPE CASTING IN PYTHON 
# Type castig is the method to convert the python variable data type into a #certain data type in order to perform required datatype .
#there are two type of type casting
#1 . Implicity
#2.  Explacity

#1. Implicit = type convertion occers when python automaticaly convert 1 #data type to another 

a=5
b=2.5
c=a+b
print(c)
print(type(c))

x=a*b
print(x)
print(type(x))

#2. Explict:- Explain type convertion is ven the programme mannualy change value data type using predefine type casting funciton.

a= (10.5)




=================================================

===============================================
15/04/26

a=256
b=256
print(id(a))
print(id(b))
print(a is b)


a=256
b=256
print(id(a))
print(id(b))
print(a is b)
print(a == b)

a="bahu"+3
print(a)


a="bahu"+"3"
print(a)

a="bahu"*"3"
print(a)

a="abhi"*3.0
print(a)

a=10%0
print(a)
==============================================
ASSIGNMENT OPERATOR

ASSIGNMENT VALUE OPERATOR ASSIGN SIDE VALUE TO LEFT SIDE

ERROR

a=10 
print(a)
10=20

a=10
a+=5
print(a)

a=10
a-=5
print(a)

a=10
a*=5
print(a)

a=10
a/=5
print(a)

NOTE:- ASSSIGNMENT OPERATOR HAVE RIGHT TO LEFT OPERATOR IN PYTHON


a=b=c=d=10
print(a,b,c,d)

ERROR

a=5
b=10
a+=b+=2

a=5
b=2
a+=b*2
print (a,b)

a=5
b=2
a//=b*3
print(a,b)

a=5
b=2
c=3
a+=b*c**2//2%3
print(a)

a=5
a*=-2
print(a)

NOTE :- SHORT HAND OPERATOR PRIORITY IS LESS

##
RELATIONAL OPERATOR():-
RELATIONAL OPERATOR ALLOW YOU TO COMPARE TOO VALUES AND RETURN A BOOLEAN RESULT EITHER TRUE OR FALSE

1. <  LESS THAN
1. >  GREATER THAN
1. <=  LESS THAN EQUal TO
1. >=  GREATER THAN EQUAL TO
1. ==  EQUAL TO
1. !=  NOT EQUAL TO


a=5
b=2
c=5
print(a==b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a!=b)

print(a>=c)
print(a!=c)
print(a<=c)

a="deepika"
b="rashmika"
print(a>b)

a="deepika"
b="rashmika"
print(a<b)


print(ord("a"))
print(ord("A"))
print(ord("@"))

#ORD function is use to get a unique code value of the single character 

print("apple" == "Apple")
print("apple"=="apple")


a=("Bdeepika")
b=("Adeepika")
print(a<b)

a=("deeA")
b=("deeB")
print(a>b)

NOTE:- 1.= STRING ARE COMPARE IN DICTONARY ORDER
2.= COMPERISTION IS DONE CHARACTER BY CHARACTER IT USES UNIQUE CODE VALUE
3.= FIRST CHRACTER DECIDE THE RESULT 

a="dog"
b="cat"
print(a>b)

print(5=='5')

a="True")
b="False")
print(a>b)

a="True"                     ERROR
b=True
print(a=b)


NOTE:- EQUALITY { == AND != } ALLOWED BETWEEN DIFFERENT TYPES BUT < , > , <= ,>= NOT ALLOWED BETWEEN INCOMPATABLE TYPE 

ERROR=========
print(5=="5")
print(5>"5")

print(True==True)
print(True==False)
print(False==False)
print(True>False)
print(True<False)
print(True<=False)
print(False<=True)


print(0==False)
print(1==True)
print(2==True)
print(""==False)
print([]==False)

NOTE:- IN PYTHON SOME VALUES ARE CONSIDERED FALISE IN CONDITION LIKE 0, "" ,[] BUT THEY DOSN'T MEAN THEY ARE EQUAL TO FALSE.

NOTE:- ALL RATIONAL OPERATOR HAVE A EQUAL PRESENDENCE THEY ARE EVALUATE LEFT TO RIGHT 

print(5>2==3)

print(10<20<30)

print(3<20!=2<5)

print(3<4!=2<5!=6==4>7!=3)

a= 10==20==30==40
print(a)

a=10==5+5==3+7==2*5
print(a)

a="a"==97
print(a)

a=10==10.0
print(a)

#LOGICAL OPERATOR ()
PYTHON LOGICAL OPERATIR

1.AND :- LOGICAL AND
2. OR :- LOGICAL OR
3. NOT :- LOGICAL NOT 

A  B    A AND B  A OR B NOT A 



print(10 and 0 or 5)

print(5>3>2)

print(bool(""))

print(10/3)

print(10//3)

===============
Indentation in python():
1. Indentation means giging proper space at the begning of a line of code.
2. it is use to define block of code
3. python dosn't use {} like java & c insted python uses indentation group statement.

Rules();
1. indentation is mendatory after collen(:)
2. all statement in the same block must have the same indentation.
3. nested block must increse indentation.
4. use constant indentation . space or tab not both.
5. indentation end block automaticaly.

a= int(input("Enter number:"))
if True:
    print ("a is even")
else
    print("b is even")




===============================================================17/04
IF ELSE():-

a=int(input("Enter the first no.:"))
b=int(input("Enter the second no.:"))
if a>b:
    print("a is greater")
else:
    print("b is greater")

1. Pass is a null statement in python it means do nothing when python see pass it execute nothing and produce no output
2. after if , else , for , while , class , etc at least one statement is compalsary inside the block with writing pass we can avoid syntax error.


a=int(input("Enter the first no.:"))
b=int(input("Enter the second no.:"))
if a>b:
    Pass
else:
    print("b is greater")


a=int(input("Enter the first no.:"))
b=int(input("Enter the second no.:"))
if a>b:
    None
else:
    print("b is greater")


NESTED IF ELSE

An if else statement retain inside another if or else block then then it is called nested if else .

if condition1:
    if condition2:
        statementx
    else:
        statementy
else
    if condition3:
        statement alpha
    else
	statement beta


#greatest of 3 number

a=int(input("Enter the first no.:"))
b=int(input("Enter the second no.:"))
c=int(input("Enter the third no.:"))

if a>b:
    if a>c:
        print("a is greater")
    else:
        print("c is greater")
else:
    if b>c:
        print("b is greater")
    else:
        print("c is greater")




# greatest of 4 number

a=int(input("Enter the first no.:"))
b=int(input("Enter the second no.:"))
c=int(input("Enter the third no.:"))
d=int(input("Enter the fourth no.:"))

if a>b:
    if a>c:
        if a>d:
            print("a is greater")
        else:
            print("d is greater")
    else:
        if c>d:
            print("c is greater")
        else:
            print("d is greater")
else:
    if b>c:
        if b>d:
            print("b is greater")
        else:
            print("d is greater")
    else:
        if c>d:
            print("c is greater")
        else:
            print("d is greater")

ex:-

age=int(input("Enter your age:"))
citizen=input("are you indian:").lower()

if age>=18:
    if citizen=="yes":
        print("You are aligible")
    else:
        print("indian required")
else:
    print("you are under age")

ex:-

username=input("Enter username :")
password=input("Enter password :").lower()

if username=="admin":
    if password=="abhi123":
        print("Login sucessful")
    else:
        print("invalid password")
else:
    print("invalid user")


Elif():-

it is a condition statement in python it is use to check multiple condition sequencelly.
it is use an after an statement


if condition1:
    statement1
elif condition2:
    statemenet2
elif condition3:
    statemenet3
elif condition4:
    statemenet4
else
    last statement


a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
c=int(input("Enter the third number :"))

if a>b and a>c:
    print("a is greater")
elif b>c:
    print("b is greater")
else:
    print("c is greater")
print("done")

   

a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
c=int(input("Enter the third number :"))
d=int(input("Enter the fourth number:"))

if a>b and a>c and a>d:
    print("a is greater")
elif b>c and b>d:
    print("b is greater")
elif b>c and b>d:
    print("b is greater")
else:
    print("c is greater")
print("done")

====================================================================
23/04/26
====================================================================

LOOPS:-
ITERATIVE STATEMENT:- loops are used for representation.

IN PYTHON THERE ARE 2 TYPESE OF LOOPS:-
1. while loop
2. for loop

1. while loop :- while loop is used to repeat a block of code as long as condition is true.

SYNTAX:-

Initialization:
while contition:
    body of loop
    increment or decrement
out of loop

example:-

i=1
while i<=5:
    print(i)
    i=i+1
print("out  of loops")

i=10
while i>=1:
    print(i)
    i-=1
print("Out")


i=20
while i>=20:
    print(i)
    i-=3
print("out")

sum of n natural number:
n=int(input("ENter the number:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i+=1
print(sum)


===
n=int(input("Enter the value:"))
i=2
while i<=n:
    print(i,end="")
    i+=2
=======

n=int(input("Enter the no."))
i=1
while i<=10:
    print(n*i)
    i+=1
=====

sum of digit

n=int(input("Enter the number:"))
sum=0
while n>0:
    rem=n%10
    sum=sum+rem
    n=n//10
print("sum is ",sum) 
======

n=int(input("n1:="))
count=0
while n>0:
    count=count+1
n=n//10
print("count=",count)

================

n1=int(input("n1:="))
n2=int(input("n2:="))

if n1>n2:
    while n1<=n2:
        print(n1)
    n1=n1+1
else:
    while n2<=n1:
        print(n1)
    n1=n1-1

==================================================================28/04/26

break keyword

i=1
while i<=10:
    print(i)
    if i==5:
        print("goted")
        break 
    i+=1


ex=2

    
    


============================================================29/04/26

s=input("Enter the string:").lower()

for ch in s:
   if ch in "aeiouAEIOU":
       continue
print(ch,end="")

===========================================================06/05/26


ex1

s=1
while s<=3:
    print("\nstudent",s)
    subject=1
    while subject<6:
        print("Subject",subject,end=" ")
        subject+=1
    s+=1

ex2

s=1
while s<=3:
    print("\nStudent",s)
    subject=1
    while subject<=6:
        print("Subject",subject,end=" ")
        chapter=1        
        while chapter<5:
            print("Chapter",chapter,end=" ")
            chapter+=1
        print()
        subject+=1
    s+=1
    print() 

ex3


for i in range(1,4):
    print("Student",i)
    for subject in range(1,6):
        print("Subject",subject,end=" ")
        for chapter in range(1,5):
            print("Chapter",chapter,end=" ")
        print()
    print()

ex4

for s in range(1,4):
    print("Student",s)
    subject=1
    while subject<=5:
        print("Subject",subject,end=" ")
        subject+=1
    print()

ex5

x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))

while x<=y:
    n=x
    flag=True
    if n>1:
        i=2
        while i<n:
            if n%i==0:
                flag=False
                break
            i+=1
        if flag==True:
            print(n) 
ex6

x=int(input("Enter the  fist number:"))
y=int(input("Enter the second number:"))

while x<=y:
    n=x
    if n>1:
        i=2
        while i<n:
            if n%i==0:
                break
            i+=1
        else:
            print(n)

ex 7

x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))

for i in range(x,y+1):
    temp=i
    power=len(str(i))
    total=0
    while temp>0:
        last=temp%10
        total=total+last**power
        temp=temp//10
    if total==i:
        print(i)
   
ex 8

x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))

for i in range(x,y+1):
    for n in range(1,11):
        print(i*n,end=" ")
    print()

====================================================================================


n=int(input("Enter n="))
i=1
while i>=n:
    print()
    j=i
    while j<=n:
        print(j,end=" ")
        j=j+1
    i=i+1

n=int(input("Enter n="))}
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        print(*,end=" ")
        j=j+1
    i=i+1

    
n=int(input("Enter n="))
i=n
while i>=1:
    print()
    dec=i
    while dec>=1:
        print(dec,end=" ")
        dec-=1
    i+=1








n=int(input("Enter n="))
i=1
while i<=n:
    print()
    j=i
    while j<=n:
        print(j,end=" ")
        j=j+1
    i=i+1


n=int(input("Enter n"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if i%2==0:
            print(*,end=" ")
        else:
            print(j,end=" ")

* 
* * 
* * * 
* * * * 
* * * * * 

n=int(input("Enter n="))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    i+=1


n=int(input("Enter n="))
i=n
while i>=1:
    print()
    j=i
    while j>=1:
        print(j,end=" ")
        j-=1
    i-=1

* * * * * 
* * * * 
* * * 
* * 
* 
n=int(input("Enter n="))
i=n
while i>=1:
    print()
    j=i
    while j>=1:
        print("*",end=" ")
        j-=1
    i-=1

1 2 3 4 5 
2 3 4 5 
3 4 5 
4 5 
5 

n=int(input("Enter n="))
i=1
while i<=n:
    print()
    j=i
    while j<=n:
        print(j,end=" ")
        j+=1
    i+=1

    
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 

n=int(input("Enter n="))
i=1
while i<=n:
    print()
    j=i
    while j<=n:
        print(i,end=" ")
        j+=1
    i+=1


n=int(input("Enter n="))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if i%2==0:
            print("*",end=" ")
        else:
            print(j,end=" ")
            j+=1
    i+=1

1 * * * * * * * * * * 1 
1 2 * * * * * * * * 2 1 
1 2 3 * * * * * * 3 2 1 
1 2 3 4 * * * * 4 3 2 1 
1 2 3 4 5 * * 5 4 3 2 1 
1 2 3 4 5 6 6 5 4 3 2 1 
n=int(input("Enter n="))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    s=1
    while s<=(n-i)*2:
        print("*",end=" ")
        s+=1
    k=i
    while k>=1:
        print(k,end=" ")
        k-=1
    i+=1
'''
n=int(input("Enter n="))
i=1
while i<=n:
    print()
    s=1
    while s<=(n-i):
        print("1",end=" ")
        s+=1
    

