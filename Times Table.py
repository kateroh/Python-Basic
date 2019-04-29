x = 1
y = 1

while x <= 9:
    y = 1
    while y <= 9:
        print("%d * %d = %d" % (x, y, x * y))
        y = y + 1
    x = x + 1