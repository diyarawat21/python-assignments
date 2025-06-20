num = int(input("Enter a number: "))

# Start with 1 (factorial of 0 is 1)
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i


print(f"The factorial of {num} is {factorial}")
