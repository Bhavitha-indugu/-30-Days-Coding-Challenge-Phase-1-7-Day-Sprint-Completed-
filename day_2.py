

# *Day - 2*  
# *Topic: Conditional Statements - Part 1*  

# 1. Check whether a number is positive. 
num=float(input("enter the number\n")) 
if num<0:
    print(num,"is not a positive number ,it is a negative number")
else:
    print(num,"is a positive number")
# 2. Check whether a number is divisible by 5.  
n1=float(input("Enter a number\n"))
if(n1%5==0):
    print(n1,"is divisible by 5")
else:
    print(n1,"is not divisible by 5")
# 3. Check whether a person is eligible to vote (age ≥ 18). 
age=int(input("Enter your age:\n")) 
if(age>=18):
    print("The person is eligible to vote")
else:
    print("The person age is less than 18,so ineligible to vote")
# 4. Check whether a number is even or odd.  
m1=int(input("Enter a number\n"))
if(m1%2==0):
    print(m1,"is even number")
else:
    print(m1,"is odd number")
# 5. Find the larger of two numbers.  
n1=float(input("Enter first number\n"))
n2=float(input("Enter second number\n"))
if(n1<n2):
    print(n2,"is larger than",n1)
else:
    print(n1,"is larger than",n2)
# 6. Check whether a student has passed or failed (pass marks = 35). 
marks=int(input("Enter marks:\n"))
if(marks>=35):
    print("student has passed the exam.")
else:
    print("student has failed the exam.")
 
# 7. Check whether a number is positive, negative, or zero.
number=float(input("Enter the number\n")) 
if(number==0):
    print("The number is zero.") 
elif(number>0):
    print(number,"is a positive number")
else:
    print(number,"is a negative number")
# 8. Check whether a person is a child, teenager, adult, or senior citizen based on age. 
age=int(input("Enter the person age:\n")) 
if(age<=12):
    print("The person is a child.")
elif(age>12 and age<20):
    print("The person is a teenager")
elif(age>19 and age<=50):
    print("The person is adult.")
else:
    print("The person is senior citizen.")

# 9. Find the largest among three numbers.
num1=float(input("enter the first number:\n")) 
num2=float(input("enter the second number:\n"))  
num3=float(input("enter the thirs number:\n"))
if(num1>num2 and num1>num3):
    print(num1,"is the largest among other 2 numbers") 
elif(num2>num1 and num2>num3):
    print(num2,"is the largest among other 2 numbers") 
else:
    print(num3,"is greater than other two numbers ")

#10.A customer is shopping in a store. If the total purchase amount is greater than ₹5000,
#the customer gets a 20% discount on the bill. Given the purchase amount, 
#calculate and print the final amount payable.
purchase_amount = int(input("Enter purchase amount\n"))

if purchase_amount > 5000:
    discount = purchase_amount * (20 / 100)
    bill = purchase_amount - discount
    print("Final amount payable by a person is:", bill)
else:
    print("Final amount payable by a person is:", purchase_amount)