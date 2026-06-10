

# *DAY 5 TOPIC*  
# loops

# *Problem 1: Sum of First N Natural Numbers*  
# Given an integer N, find the sum of the first N natural numbers. 
num=int(input("Enter a number:\n")) 
sum=0
for i in range(1,num+1):
    sum=sum+i
print("Sum of first N natural numbers",sum)

# *Problem 2: Multiplication Table*  
# Given an integer N, print its multiplication table from 1 to 10. 
a=int(input("Enter a number:\n")) 
for i in range(1,11):
    print(a,"*",i,"=",a*i)

# *Problem 3: Count Digits in a Number*  
# Given a positive integer N, count the total number of digits present in the number.
# b=input("Enter a number:\n")
# print("No of digits in a number is:",len(b))
n = input("Enter a positive integer: ")

count = 0

for digit in n:
    count += 1

print("Total number of digits:", count)
  

# *Problem 4: Reverse a Number*  
# Given an integer N, reverse its digits and print the resulting number.
N=int(input("Enter a number:\n"))
def reverse_number(N):
    reversed=0
    while N>0:
        last_digit=N%10
        reversed=(reversed*10)+last_digit
        N=N//10
    print(reversed)
reverse_number(N)
    


# *Problem 5: Check Prime Number*  
# Given an integer N, determine whether the number is prime or not. 
d = int(input("Enter a number:\n"))

for i in range(2, d):
    if d % i == 0:
        print(d, "is not a prime number")
        break
else:
    print(d, "is a prime number")