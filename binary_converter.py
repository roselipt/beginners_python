#  Convert to decimal to binary and back

l = [1, 8, 13, 32, 33, 34, 0]

for decimal in l :
    power = 0
    binary = []
    print(decimal, "in binary is ", end='')
    while decimal > 2 ** power :
        power += 1
    while power >= 0 :
        if 2 ** power <= decimal :
            binary += [1]
            decimal -= 2 ** power
        else :
            binary += [0]
        power -= 1
    print(binary)

    # for exp in range(power, -1, -1)
    #     if 2 ** exp 
    #     digit = 1 if (decimal DIV 2)
    # while decimal > 0 :
    #     digit = decimal % (2**(power+1))
    #     binary = [digit] + binary
    #     decimal -= digit * 2 ** power
    #     power += 1
    # print(binary)