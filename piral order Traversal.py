##spiral order Traversal
##spiral order pattern
'''n=int(input("Enter the size:"))
a=[[0] *n for _ in range(n)]
top=0
bottom=n-1
left=0
right=n-1
num=1
while top<=bottom and left<=right:
    #traverse from left to right
    for i in range(left,right+1):
        a[top][i]=num
        num+=1
    top+=1
    #traverse from top to bottom
    for i in range(top,bottom+1):
        a[i][right]=num
        num+=1
    right-=1
    #traverse from right to left
    for i in range(right,left-1,-1):
        a[bottom][i]=num
        num+=1
    bottom-=1
        #traverse from bottom to top
    for i in range(bottom,top-1,-1):
        a[i][left]=num
        num+=1
    left+=1
for row in a:
    for val in row:
        print(f"{val:3}",end=" ")
    print()
print("spiral order traversal of the matrix:")
for i in range(n):
    for j in range(n):
        print(a[i][j],end=" ")
    print()'''


r=int(input("Enter the number of rows: "))
c=int(input("Enter the number of columns: "))
a=[]
print("Enter the elements ")
for i in range(r):
    row = []
    for j in range(c):
        element = int(input())
        row.append(element)
    a.append(row)
top = 0
bottom = r - 1
left = 0
right = c - 1
while top <= bottom and left <= right:
    # Left to right
    for i in range(left, right + 1):
        print(a[top][i], end=" ")
    top += 1

    # Top to bottom
    for i in range(top, bottom + 1):
        print(a[i][right], end=" ")
    right -= 1

    # Right to left
    for i in range(right, left - 1, -1):
        print(a[bottom][i], end=" ")
    bottom -= 1

    # Bottom to top
    for i in range(bottom, top - 1, -1):
        print(a[i][left], end=" ")
    left += 1