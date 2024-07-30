def is_armstrong(n):
    order = len(str(n))
    temp = n
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    return n == sum    

number = int(input("Enter a number: "))
if is_armstrong(number):
    print("Armstrong number.")
else:
    print("Not an armstrong number.")    
    