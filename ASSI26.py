age_h = int(input("Input a dog's age in human years: "))

if age_h < 0:
    print("Age must be positive number.")
    exit()
elif age_h <= 2:
    age_d = age_h * 10.5
else:
    age_d = 21 + (age_h - 2)*4

print("The dog's age in dog's years is", age_d)
