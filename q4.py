start = 1
stop = 10

sum_odd = 0

for num in range(start, stop + 1):
    if num % 2 != 0:  
        sum_odd += num

print("Sum of odd numbers:", sum_odd)
