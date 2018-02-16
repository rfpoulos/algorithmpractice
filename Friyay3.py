def numberfinder(input_number):
    count = input_number
    test = False
    for x in range(input_number, (input_number/2), -1):  
        i = 1
        while test == False:
            for number in range(input_number, 1, -1):
                if (i * count) % (x - 1) != 0:
                    i += 1
                else:
                    count = (i * count)
                    count += count
                    break
    return count

print numberfinder(20)
