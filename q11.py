num=987

while num>=10:
    sum_of_digits=0
    for digit in str(num):
        sum_of_digits += int(digit)
    num = sum_of_digits

print("Final Output:", num)