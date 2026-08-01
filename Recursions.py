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
'''def tail(n):
    if n == 0:
        return
    print(n, end=" ")
    tail(n - 1)
print("Enter a value: ")
n=int(input())
tail(n)'''

## 4.Head Recursion
'''def head(n):
    if n == 0:
        return
    head(n - 1)
    print(n, end=" ")
print("Enter a value: ")
n=int(input())
head(n)'''

## 5.Tree Recursion fibonacci number
'''def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
n=int(input("Enter a value: "))
print(fib(n))'''

## 6.Nested Recursion
def nested(n):
    if n > 100:
        return n - 10
    return nested(nested(n + 11))
print("Enter a value: ")
n=int(input())
print(nested(n))