def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("GCD: ", gcd(num1, num2))    