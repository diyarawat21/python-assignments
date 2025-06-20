num=int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("BRUDITE - NIRVANA")
elif num % 3 == 0:
    print("SKILLBREW")
elif num % 5 == 0:
    print("BRUDITE")
else:
    print("Not divisible by 3 or 5")
