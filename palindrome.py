def paltest():
    for i in range(999, 100, -1):
        pal_test = str(i * i)
        if pal_test == pal_test[::-1]:
            return i * i
        else:
            pal_test = str(i * (i - 1))
            if pal_test == pal_test[::-1]:
                return i * i

print paltest()