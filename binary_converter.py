#  Convert to decimal to binary and back

l = [1, 8, 13, 32, 33, 34, 49, 0]

for decimal in l :
    power = 0
    binary = []
    print(decimal, "in binary is ", end='')
    while decimal >= 2 ** power :
        power += 1
    #print('(power between loops is', power, ') and', decimal > 2 ** power)
    while power >= 0 :
        binary_digit = decimal // 2 ** power
        decimal = decimal % 2 ** power
        
        binary += [binary_digit]
        power -= 1
    print(binary)

for decimal in l:
    target = []
    num = decimal
    place = 0
    while num > 0:
        power = 2 ** (place + 1)
        div = num // power
        mod = num % power
        #print(place, num, div, mod, mod == 2 ** power)
        if mod == 2 ** place:
            target = [1] + target
            num -= mod
        else:
            target = [0] + target
        place += 1
    print(decimal, 'the other way is', target)

    #  This block works: I wrote it first and then improved readability above ... or did I?
    # while power >= 0 :
    #     if 2 ** power <= decimal :
    #         binary += [1]
    #         decimal -= 2 ** power
    #     else :
    #         binary += [0] if (binary or power ==0) else []
    #     power -= 1

    # for exp in range(power, -1, -1)
    #     if 2 ** exp 
    #     digit = 1 if (decimal DIV 2)
    # while decimal > 0 :
    #     digit = decimal % (2**(power+1))
    #     binary = [digit] + binary
    #     decimal -= digit * 2 ** power
    #     power += 1
    # print(binary)