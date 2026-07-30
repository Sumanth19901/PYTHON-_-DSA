#-functions are in four types
## 1.Argument pass return value
'''def summate(a,b):
    return a+b
num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
result=summate(num1,num2)
print("The sum of two numbers is: ",result)'''

## 2.argument pass but no-return value
'''def summate1(n1,n2):
    print("The sum of two numbers is: ",n1+n2)
n1=int(input("Enter a number: "))
n2=int(input("Enter another number: "))
summate1(n1,n2)
'''

## 3.no-argument but returnvalue
'''def summate2():
    n1=int(input("Enter a number: "))
    n2=int(input("Enter another number: "))
    return n1+n2
result=summate2()
print("The sum of two numbers is: ",result)'''


## 4.no-argument no-returnvalue
'''def summate3():
    n1=int(input("Enter a number: "))
    n2=int(input("Enter another number: "))
    print("The sum of two numbers is: ",n1+n2)
summate3()'''