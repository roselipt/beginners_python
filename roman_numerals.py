number = int(input("Enter a number "))

print("Thank you,", number)

rules = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400,'CD'),(100,'C'), (90, 'XC'), \
        (50, 'L'),(40, 'XL'),(10, 'X'),(9, 'IX'),(5, 'V'),(4, 'IV'), (1, 'I')]

remaining = number
s = ''
for val, symbol in rules:
    while remaining >= val:
        s += symbol
        remaining -= val

print('number is',s)