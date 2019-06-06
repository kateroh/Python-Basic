# Power
for i in range(11):
    print("2^%d = %d" % (i, (2**i)))

# Times table using for
for i in range(1, 10):
    for j in range(1, 10):
        print("%d * %d = %d" % (i, j, i * j))

# Practice range
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

for i in range(0, 8):
    print(i, numbers[i])