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


## 3.Tail Recursion
## 4.Head Recursion
## 5.Tree Recursion fibonacci number
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
n=int(input("Enter a value: "))
print(fib(n))
## 6.Nested Recursion