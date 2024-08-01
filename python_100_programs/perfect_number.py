def is_perfect_number(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += 1
    return sum == n

number = int(input("enter a number: "))
if is_perfect_number(number):
    print("Perfect number")
else:
    print("Not a perfect number")            