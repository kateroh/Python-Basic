n = 120
count = 0
i = 1

while i <= 120:
    if n % i == 0:
        count += 1
        print(i)

    i += 1

print("%d의 약수는 총 %d개 입니다." % (n, count))