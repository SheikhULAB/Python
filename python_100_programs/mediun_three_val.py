def find_median(a,b,c):
    return sorted([a,b,c])[1]

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

print("Median: ", find_median(num1, num2, num3))