num = 12345
revnum = 0

while num > 0:
    digit = num % 10         # Get the last digit
    revnum = revnum * 10 + digit  # Add digit to reversed number
    num = num // 10          # Remove last digit

print("Reversed number is:", revnum)
