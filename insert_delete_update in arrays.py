#insert/delete/update in arrays
array=int(input("Enter the number of elements in the array: "))
arr=[]
for i in range(array):
    val=int(input("Enter element "))
    arr.append(val)
print("The array is: ")
for i in range(array):
    print(arr[i],end=" ")
print("\n")

pos=int(input("Enter the position where you want to insert the element: "))
value=int(input("Enter the value of position : "))
arr.insert(pos,value)
print("latest array : ")
for i in arr:
    print(i,end=" ")
print("\n")

pos=int(input("Enter the position where you want to delete the element: "))
arr.pop(pos)
print("latest array : ")
for i in arr:
    print(i,end=" ")
print("\n")
