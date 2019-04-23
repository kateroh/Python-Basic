def print_grade(midterm, final):
    total = midterm + final
    if total >= 90:
        print("You get an A")
    elif 80 <= total < 90:
        print("You get a B")
    elif 70 <= total < 80:
        print("You get a C")
    elif 60 <= total < 70:
        print("You get a D")
    else:
        print("You fail")


print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)