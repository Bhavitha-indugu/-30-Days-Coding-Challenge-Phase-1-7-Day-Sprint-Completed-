

# # *Day - 7*  
# # *Topic: List + Loops - Part 2*  

# # 1. Given a list of integers, find the index of the largest element. 
# arr=list(map(int,input().split()))
# max_element=arr[0]
# max_index=0
# for i in range(1,len(arr)):
#     if arr[i]>max_element:
#         max_element=arr[i]
#         max_index=i
# print("Max element index:",max_index)

# # 2. Given a list of integers, count how many times the largest element appears.
# a=list(map(int,input().split()))
# max_element=a[0]
# count=0
# for i in range(1,len(a)):
#     if a[i]>max_element:
#         max_element=a[i]
# for i in range(1,len(a)):
#     if a[i]==max_element:
#         count=count+1
# print(count)

# # 3. Given a list of integers, check if the list is sorted in ascending order.
# a=list(map(int,input("enter a list of elements with spaces in a single line").split())) 
# sorted=True
# for i in range(len(a)-1):
#     if a[i]>a[i+1]:
#         sorted=False
#         break
# if sorted==True:
#     print("The given list is in ascending order")
# else:
#     print("The given list is not in ascending order")


# # 4. Given a list of integers & a key, check if key exists in the array  
# list=list(map(int,input("Enter the list of elements with spaces in a single line:\n").split()))
# key=int(input("Enter the value of key:\n"))
# found=False
# for i in range(len(list)):
#     if list[i]==key:
#         found=True
#         break
# if found==True:
#     print("key exists in the list",key)       
# else:
#     print("key doesn't exists in the list")
# 5. Given a list of integers, find the difference between the sum of even numbers
# and the sum of odd numbers.  
l=list(map(int,input().split()))
sum_of_even=0
sum_of_odd=0
for i in l:
    if i%2==0:
        sum_of_even=sum_of_even+i
    else:
        sum_of_odd=sum_of_odd+i
difference=sum_of_even-sum_of_odd
print("difference between sum of even and odd numbers is:",difference)

# 6. Given a list of integers, remove all occurrences of a given number and print the 
# updated list. 
l = list(map(int, input("Enter list elements:\n").split()))
key = int(input("Enter number to remove:\n"))

new_list = []

for num in l:
    if num != key:
        new_list.append(num)

print("Updated list:", new_list) 
# 7. Given a list of integers, create a new list where each element is doubled and print 
# the result.
l=list(map(int,input().split()))
new_list=[]
for i in l:
    new_list.append(i*i)
print(new_list)
