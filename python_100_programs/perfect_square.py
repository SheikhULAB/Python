import math

def is_perfect_square(n):
    root = math.isqrt(n)
    return root * root == n

number = int(input("Enter a number: "))

if is_perfect_square(number):
    print("Perfect Square.")
else:
    print("Not a perfect square.")    