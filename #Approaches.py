#Approaches
#1.math
'''n=int(input("Enter a value: "))
if n%2==0:
    print("Even")
else:
    print("Odd")'''

#2.naive
'''arr=list(map(int,input("Enter a list of numbers: ").split()))
largest=arr[0]
for i in range(len(arr)):
    if arr[i]>largest:
        largest=arr[i]
print("Largest number is:", largest)'''

#3.brute force
'''arr=list(map(int,input("Enter a list of numbers: ").split()))
target=int(input("Enter a target value: "))
found=False
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print("Pair found:", arr[i], "and", arr[j])
            found=True
        if found:
            break
if not found:
    print("No pair found")'''

#4.greedy
'''coins=list(map(int,input("Enter coin denominations: ").split()))
target=int(input("Enter a target value: "))
print("Coins used to make the target value:")
for coin in coins:
    while target>=coin:
        print(coin, end=" ")
        target-=coin'''

#5.Backtracking
def generate(s,n):
    if len(s) == n:
        print(s)
        return
    generate(s + "0", n )
    generate(s + "1", n)
n=int(input("Enter length: "))
generate("", n)