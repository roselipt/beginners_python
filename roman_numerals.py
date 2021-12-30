number = int(input("Enter a number "))

print("Thank you,", number)
remaining = number
roman = ''
if remaining >= 50:
    fifties = remaining // 50
    roman += fifties * 'L'
    remaining = remaining % 50
if remaining == 40:
    roman += 'XL'
    remaining -= 40
if remaining >= 10:
    tens = remaining // 10
    roman += 'X'* tens
    remaining %= 10
if remaining == 9:
    roman += 'IX'
    remaining -= 9
if remaining >= 5:
    roman += 'V'
    remaining -= 5
if remaining == 4:
    roman += 'IV'
    remaining -= 4
#  Take this if out, but think about it first
if remaining >= 1:
    roman += 'I'*remaining
    remaining = 0    

print(number, 'is', roman, 'plus', remaining, 'left.')
