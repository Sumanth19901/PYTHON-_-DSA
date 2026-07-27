#write a code to print the even and odd digits of the given number
n=int(input("Enter a number: "))
even_sum=0
odd_sum=0
while n!=0:
    d=n%10
    if d%2==0:
        even_sum+=1
    else:
        odd_sum+=1
    n//=10
print("The sum of even digits is:", even_sum)
print("The sum of odd digits is:", odd_sum)