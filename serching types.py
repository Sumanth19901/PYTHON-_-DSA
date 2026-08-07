#Searching Types
##1.linear Search
'''arr=list(map(int,input("Enter Elements: ").split()))
target=int(input("Enter Target Element: "))
for i in range(len(arr)):
    if arr[i]==target:
        print("Element Found at index: ",i)
        break'''
##2.binary Search
'''arr=list(map(int,input("Enter Elements: ").split()))
target=int(input("Enter Target Element: "))
low=0
high=len(arr)-1
while low <= high:
    mid=(low+high)//2
    if arr[mid]==target:
        print(target,"Element Found at index: ",mid)
        break
    elif arr[mid]<target:
        low=mid+1
    else:
        high=mid-1'''
##3. jump Search
import math
arr=list(map(int,input("Enter Elements: ").split()))
target=int(input("Enter Target Element: "))
n=len(arr)
step=int(math.sqrt(n))
prev=0
found=False
while arr[min(step,n)-1]<target:
    prev=step
    step+=int(math.sqrt(n))
    if prev>=n:
        break
while prev<min(step,n):
    if arr[prev]==target:
        print("Element Found at index: ",prev)
        found=True
        break
    prev+=1
if not found:
    print("Element Not Found")
##4. exponential Search
##5. interpolation Search
##6. Fibonacci Search
##7. ternary Search
##8. sublist Search
##9. sentinel Search