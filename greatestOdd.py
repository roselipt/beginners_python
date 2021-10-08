#  Ask user to input 10 numbers and then print the greatest odd

numbers = [1,2,3,4,5]

def odd(arg) :
    if arg % 2 == 0 :
        return False
    else :
        return True

oddNumbers = []

for i in numbers :
    if odd(i) :
        oddNumbers.append(i)

greatestOdd = oddNumbers[0]
for i in numbers :
    if i > greatestOdd :
        greatestOdd = i

print("Greatest odd is", i)

print("And if my grandmother had wheels she'd be a wagon.")