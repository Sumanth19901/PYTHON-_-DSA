#write a code to find the sum of a give number
n=int(input("Enter a number: "))
sum=0
while n!=0:
    d=n%10
    sum+=d
    n//=10
print("The sum of the digits is:", sum)