#----Array Data Structure 1-D----#
#array data structure is a linear DS
#1.read and write an array
'''n=int(input("Enter the size of the array: "))
arr=[]
for i in range(n):
    num=int(input("Enter a number: "))
    arr.append(num)
#arr=list(map(int,input("Enter a list of numbers: ").split()))
print("The array is:")
for i in range(n):
    print(arr[i], end=" ")
#print(*arr)'''


#2.find the sum off array
'''n=int(input("Enter the size of the array: "))
arr=[]
sum=0
for i in range(n):
    num=int(input("Enter a number: "))
    arr.append(num)
print("The array is:")
for i in range(n):
    sum+=arr[i]
print("The sum of the array is:", sum)'''

#3.find the average
'''n=int(input("Enter the size of the array: "))
arr=[]
sum=0
for i in range(n):
    num=int(input("Enter a number: "))
    arr.append(num)
    sum+=num
print("The array is:")
for i in range(n):
    print(arr[i], end=" ")
print()
print("The sum of the array is:", sum)
print("The average of the array is:", sum/n)'''

#4.find the largest/smallest element in an array
'''n=int(input("Enter the size of the array: "))
arr=[]
for i in range(n):
    num=int(input("Enter a number: "))
    arr.append(num)
print("The array is:")
for i in range(n):
    print(arr[i], end=" ")
print()
print("The largest element in the array is:", max(arr))
print("The smallest element in the array is:", min(arr))'''

#5.count the even and odd numbers/prime
n=int(input("Enter the size of the array: "))
arr=[]
for i in range(n):
    num=int(input("Enter a number: "))
    arr.append(num)
num_even=0
num_odd=0
for i in range(n):
    if arr[i]%2==0:
        num_even+=1
    else:
        num_odd+=1
print("The number of even numbers in the array is:", num_even)
print("The number of odd numbers in the array is:", num_odd)
#6.count pos/neg
#7.reverse an array
#8.left rotate
#9.right rotate
#10.array using strings
