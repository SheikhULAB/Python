a = 12

a > 15
False

a > 10
True

a > 10 and a < 13
True

not a > 15
True

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5.")
    elif age <=18:
        print("Please pay $7.")
    elif age >= 45 and age <=55:
        print("Everything is going to be ok. Have a free ride on us!")    
    else:
        print("Please play $12.")    
else:
    print("Sorry, you have to grow taller before you can ride.")    