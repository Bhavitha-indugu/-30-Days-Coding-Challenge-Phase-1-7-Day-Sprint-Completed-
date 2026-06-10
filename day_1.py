#1.Write a program to print-Let's start the challenge ,I will stay consistent
print("let's start the challenge, I will stay consistent.")

# 2. Take your name as a input and print a welcome message.
Name = input("enter your name?")
print("welcome"+" "+Name+"!")
print(f'welcome {Name}!')

#3.Take two numbers as input and print their sum.
num1=int(input("enter the first number?"))
num2=int(input("enter the second number?"))
sum=num1+num2
print("sum of two numbers is:",sum)

#4.Take two numbers as input and print their remainder.
n1=int(input("Enter first number?\n"))
n2=int(input("Enter second number?\n"))
remainder=n1%n2
print("remainder of two numbers are:",remainder)

#5.Take three numbers as input and calculate their average.
a1=int(input("Enter first number\n"))
a2=int(input("Enter second number\n"))
a3=int(input("Enter third number\n"))
average=(a1+a2+a3)/3
print("Average of 3 input numbers is:",average)

#6. Take 2 numbers as input and swap their values
val1=int(input("enter the number 1\n"))
val2=int(input("enter number 2\n"))
val1,val2=val2,val1
print("After swapping")
print("val1=",val1)
print("val2=",val2)

#7.take marks of 5 subjects as input and calculate the total marks and percentage
sub1=float(input("enter subject 1:"))
sub2=float(input("enter subject 2:"))
sub3=float(input("enter subject 3:"))
sub4=float(input("enter subject 4:"))
sub5=float(input("enter subject 5:"))
total=sub1+sub2+sub3+sub4+sub5
percentage=(total/500)*100
print("total marks are:",total)
print("percentage is:",percentage)

#8.take a temp in celsius and convert it into farenheit
celsius=float(input("enter temperature in celsius\n"))
farenheit=(celsius*9/5)+32
print(celsius,"celcius to farenheit",farenheit)

#9.take a temp in farenheit and convert it into celsius
farenheit=float(input("enter temp in fareheit\n"))
celsius=(farenheit-32)*5/9
print(farenheit,"farenheit to celsius",celsius)

#10.take a length, breadth and height of a cuboid as input and calculate its volume
length=float(input("enter length of a cuboid\n"))
breadth=float(input("enter breadth of a cuboid\n"))
height=float(input("enter height of a cuboid\n"))
volume=length*breadth*height
print("volume of a cuboid is:",volume)

