## Recursions (base, recursion) ##
## 1.Direct
'''def numbers(n):
    if n == 0:
        return
    print(n ,end=" ")
    numbers(n - 1)
n=int(input("Enter a value: "))
numbers (n)'''


## 2.indirect
'''def even(n):
    if n == 0:
        return
    odd(n - 1)
def odd(n):
    if n == 0:
        return
    even(n - 1)
n=int(input("Enter a value: "))
even(n)'''


## 3.Tail
## 4.Head
## 5.Tree
## 6.Nest