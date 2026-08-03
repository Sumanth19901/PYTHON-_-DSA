#reverse an array
'''n=int(input("Enter the number of elements in the array: "))
arr=[]
for i in range(n):
    val=int(input("Enter element "))
    arr.append(val)
print("Original array: ", arr)
for i in arr:
    print(i, end=" ")
print()
print("Reversed array: ")
i=n-1
while i>=0:
    print(arr[i], end=" ")
    i-=1'''

#code to rotate an array to left
'''n=int(input("Enter the number of elements in the array: "))
arr=[]
for i in range(n):
    val=int(input("Enter element "))
    arr.append(val)
print("Original array: ")
for i in arr:
    print(i, end=" ")
print()
print("Array after left rotation: ")
first=arr[0]
for i in range(0, n-1):
    arr[i]=arr[i+1]
arr[n-1]=first
for i in arr:
    print(i, end=" ")'''

n=int(input("Enter the number of elements in the array: "))
arr=[]
for i in range(n):
    val=int(input("Enter element "))
    arr.append(val)
print("Original array: ")
for i in arr:
    print(i, end=" ")
print()
print("Array after right rotation: ")
last=arr[n-1]
for i in range(n-1, 0, -1):
    arr[i]=arr[i-1]
arr[0]=last
for i in arr:
    print(i, end=" ")

