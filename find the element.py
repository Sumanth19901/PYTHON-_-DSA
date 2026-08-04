#a=2,5,8,10,15,16
'''arr=[]
n=int(input("enter the size of the array:"))
print("enter the elements of the array:")
for i in range(n):
    arr.append(int(input()))
target=int(input("enter the target value:"))
if target in arr:
    print("target value is present in the array")
else:
    print("target value is not present in the array")'''

#a=2,5,8,10,15,16
arr=[]
n=int(input("enter the size of the array:"))
print("enter the elements of the array:")
for i in range(n):
    arr.append(int(input()))
target=int(input("enter the target value:"))
found=False
for i in range(n):
    if arr[i]==target:
        print(target,"found at index",i)
        found=True
        break
if not found:
    print("target value is not present in the array")