# Question : Use the while and if statements to print all of the natural numbers
# below 100 that are multiples of 8 but not multiple of 12.

i = 1
while i <= 100:
    if (i % 8) == 0 and (i % 12) != 0:
        print(i)
        i += 1
    else:
        i += 1