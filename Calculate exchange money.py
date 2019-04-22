def calculate_change(payment, cost):
    change = payment - cost
    fify_thousand_count = int(change / 50000)

    change = change % 50000
    ten_thousand_count = int(change / 10000)

    change = change % 10000
    fify_hundred_count = int(change / 5000)

    change = change % 5000
    ten_hundred_count = int(change / 1000)

    print("50000원 지폐: %d장" % fify_thousand_count)
    print("10000원 지폐: %d장" % ten_thousand_count)
    print("5000원 지폐: %d장" % fify_hundred_count)
    print("1000원 지폐: %d장" % ten_hundred_count)


calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)