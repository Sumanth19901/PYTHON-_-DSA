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