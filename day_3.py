
# # *Day - 3*  
# # *Topic: Logical Operators & Conditional Statements*  

# # 1. Check whether a number is divisible by both 3 and 5.  
# num=float(input("Enter a number:\n"))
# if(num%3==0 and num%5==0):
#     print(num,"is divisible by both 3 and 5")
# else:
#     print(num,"is not divisible by both 3 and 5")
# # 2. Check whether an ATM withdrawal can be processed based on available balance
# #  and withdrawal amount.  
# balance=float(input("Enter balance amount:\n"))
# withdrawal=float(input("Enter withdrawal amount:\n"))
# if(withdrawal<=balance):
#     print("withdrawal of money is sucessfull.")
# else:
#     print("Insufficient balance,withdrawal of money is not processed.")

# # 3. Check whether a student is eligible for admission if they have either:  
# #    a. Marks ≥ 70 OR  
# #    b. A sports quota certificate.
marks=float(input("Enter marks of a student:\n"))
sports_quota=input("Do you have any sports quota certificate?(yes/no):")
s=sports_quota.lower()
if(marks>=70 or s=='yes'):
    print("Student is eligible for admission")
else:
    print("Student is not eligible for admission.")
  
# 4. Determine whether a year is a leap year.
year = int(input("Enter a year:\n"))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

