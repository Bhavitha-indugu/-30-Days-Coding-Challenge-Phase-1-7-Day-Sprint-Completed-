  

# *Day - 6*  
# *Topic: List + Loops - Part 1*  

# 1. Given an array of integers, print all the elements of the array. 
arr=[1,2,3,4,5,6,7,8,9] 
for a in arr:
    print(a)
# 2. Given an array of integers, find and print the sum of all elements. 
a=[9,8,6,8,5,7] 
sum=0
for i in a:
    sum=sum+i
print("sum of integers in array is:",sum)
# 3. Given an array of integers, find and print the largest element.  
array=[45,67,89,90,45,23,66]
print("Largest element in the given array is:",max(array))
# 4. Given an array of integers, find and print the smallest element.  
array=[45,67,89,90,45,23,66]
print("Largest element in the given array is:",min(array))
# 5. Given an array of integers, count how many even numbers are present. 
b=[2,3,45,56,78,99,87,66,23,6,8] 
count=0
for i in b:
    if i%2==0:
        count=count+1
    else:
        count=count+0
print("Number of even numbers in the given array is:",count)
# 6. Given an array of integers, print only the odd numbers.
d=[3,4,5,6,879,45,67,89,0,33,56,22]  
for i in d:
    if i%2!=0:
        print(i)
# 7. Given an array of integers, count how many elements are greater than 10.  
e=[1,2,3,4,5,78,11,15,6,34]
count=0
for i in e:
    if i>10:
        count=count+1
    else:
        count=count+0
print("Number of elements greater that 10 are:",count)

# 8. Given an array of integers, create a new array containing the square of each element 
# and print it. 
f=[1,2,3,4,56,6,7,8] 
a=[]
for i in f:
    b=i*i
    a.append(b)
print(a)
# 9. Given an array of integers, print the elements in reverse order.  
g=[1,2,3,4,5,6,7,8,9,0]
print(g[: :-1])#using slicing
    
# 10. Given an array of integers, find the average of all elements.  
h=[2,3,4,5,6,7,8,1]
sum=0
for i in h:
    sum=sum+i
average=sum/len(h)
print("Average of the elements in array  is:",average)

