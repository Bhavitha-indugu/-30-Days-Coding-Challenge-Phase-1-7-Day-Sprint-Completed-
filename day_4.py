

# *Day - 4*  
# *Topic: Loops*  

# 1. *Print Numbers from 1 to 1000*  
#    Write a Python program that uses a loop to print all numbers from 1 to 1000, each on a
# new line.  
for i in range(1,1001):
    print(i)

# 2. *Print the Multiplication Table of a Number*  
#    Write a Python program that takes an integer N as input and prints its multiplication
# table up to 10 terms.  
number=int(input("Enter a Number:\n"))
for i in range(1,11):
    print(number,"*",i,"=",number*i)

# 3. *Print All Even Numbers from 1 to N*  
#    Write a Python program that takes an integer N as input and prints all even numbers from 
# 1 to N. 
num=int(input("Enter a number:\n"))
for i in range(2,num+1):
    if(i%2==0):
        print(i)


# 4. *Print All Odd Numbers from 1 to N*  
#    Write a Python program that takes an integer N as input and prints all odd numbers 
# from 1 to N. 
a=int(input("Enter a number:\n")) 
for i in range(1,a+1):
    if i%2!=0:
        print(i)

# 5. *Find the Factorial of a Number*  
#    Write a Python program that takes an integer N as input and calculates the factorial 
# of N using a loop. 
b=int(input("Enter a number:\n"))
factorial=1
for i in range(1,b+1):
    factorial=factorial*i
print("factorial of",b,"is",factorial)



