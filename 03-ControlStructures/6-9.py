age = int(input("Enter the dog's age in human years: "))

if age <= 2:
    dog_age = age * 10.5
else:
    dog_age = 2 * 10.5 + (age - 2) * 4

print(f"The dog's age in dog's years is {dog_age:.0f} years.")
