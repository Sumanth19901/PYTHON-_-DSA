#Approaches
#1.math
'''n=int(input("Enter a value: "))
if n%2==0:
    print("Even")
else:
    print("Odd")'''

#2.naive
arr=list(map(int,input("Enter a list of numbers: ").split()))
largest=arr[0]
for i in range(len(arr)):
    if arr[i]>largest:
        largest=arr[i]
print("Largest number is:", largest)
#3.brute force
#4.greedy
#5.Backtracking