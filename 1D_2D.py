#1D data stuctures
'''n = int(input("Enter a value:\n"))               
for i in range(n):
    print(i,end=" ")'''

#2D data structures 
#hollow square
'''n=int(input("Enter a value: "))
for i in range(n):
    for j in range(n):
        if 1==0 or i==n-1 or j==0 or j==n-1 or j==i or j==n-i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#Hour glass
'''n=int(input("Enter a value: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==j or (i+j)==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#butterfly
'''n=int(input("Enter a value: "))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j or (i+j)==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#plese simble
'''n=int(input("Enter a value: "))
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#dimond
n=int(input("Enter a value: "))
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2 or i+j==n//2 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()