def sum_of_natural_numbers(n):
    if n <= 1:
        return n
    else:
        return n + sum_of_natural_numbers(n - 1)
    
num = int(input("Enter a number: "))

print("Sum of natural number: ", sum_of_natural_numbers(num))    