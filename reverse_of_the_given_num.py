#write the code to print the reverse of the number
n=int(input("Enter a number: "))
reverse=0
while n!=0:
    d=n%10
    reverse=reverse*10+d
    n//=10
print("The reverse of the number is:", reverse)