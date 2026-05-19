#  recursion - function calling itself

# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(200)
# print(sys.getrecursionlimit())

### direct recursion
def natural(n):
    if n == 0:
        return # just return keyword stops the function
    print(n, end=" ")
    return natural(n-1)

# natural(10)
# print()

##### indirect recursion

def num(n):
    if n<=0:
        return
    print(n, end=" ")
    num1(n-1)
def num1(n):
    print(n, end=" ")
    num(n-1)

# num1(10)

# factorial using recursion
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

print(fact(5))

# recursion : check if number is prime or not  ->  prime numbers : divided by 1 and itself , eg: 11, 3, 5, 7, 13

def is_prime(n, i=2):
    # Base cases
    if n <= 1:
        return False
    if i == n:
        return True
    
    # If divisible → not prime
    if n % i == 0:
        return False
    
    # Check next divisor
    return is_prime(n, i + 1)


# print(is_prime(11))  # True
# print(is_prime(10))  # False


# fabonacci series 

def fib(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)


print(fib(6))  # 8


