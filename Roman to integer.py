def value(x):
    if (x == 'I'):
        return 1
    if (x == 'V'):
        return 5
    if (x == 'X'):
        return 10
    if (x == 'L'):
        return 50
    if (x == 'C'):
        return 100
    if (x == 'D'):
        return 500
    if (x == 'M'):
        return 1000
    return -1


def roman_integer(str):
    y = 0
    z = 0

    while (z < len(str)):

        s1 = value(str[z])

        if (z + 1 < len(str)):

            s2 = value(str[z + 1])

            if (s1 >= s2):

                y = y + s1
                z = z + 1
            else:

                y = y + s2 - s1
                z = z + 2
        else:
            y = y + s1
            z = z + 1

    return y

print("The Numeral from Integer to Roman is", roman_integer("V"))