n = int(input("Enter the size: "))

a = [[0] * n for _ in range(n)]

top = 0
bottom = n - 1
left = 0
right = n - 1

num = n * n

while top <= bottom and left <= right:

    # Left to right
    for i in range(left, right + 1):
        a[top][i] = num
        num -= 1
    top += 1

    # Top to bottom
    for i in range(top, bottom + 1):
        a[i][right] = num
        num -= 1
    right -= 1

    # Right to left
    for i in range(right, left - 1, -1):
        a[bottom][i] = num
        num -= 1
    bottom -= 1

    # Bottom to top
    for i in range(bottom, top - 1, -1):
        a[i][left] = num
        num -= 1
    left += 1

# Print matrix
print("Spiral order traversal of the matrix:")
for row in a:
    for val in row:
        print(f"{val:3}", end=" ")
    print()