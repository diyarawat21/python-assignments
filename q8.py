number1 = 12
number2 = 18

if number1 > number2:
    greater = number1
else:
    greater = number2

while True:
    if (greater % number1 == 0) and (greater % number2 == 0):
        lcm = greater
        break
    greater += 1

print(f"LCM of {number1} and {number2} is: {lcm}")
