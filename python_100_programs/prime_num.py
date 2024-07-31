def generate_primes(start, end):
    primes = []
    for num in range(start,end + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
        else:
            primes.append(num)
    return primes                

start_range = int(input("Enter the starting range:"))
end_range = int(input("Enter the ending range: "))

print("Prime numbers: ",generate_primes(start_range, end_range))