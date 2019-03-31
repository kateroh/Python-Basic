from random import randint


# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    random_num = []
    for i in range(6):
        num = randint(1, 45)
        while num in random_num:
            num = randint(1, 45)
        random_num.append(num)
    random_num.sort()
    return random_num


# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# 예: [1, 7, 13, 23, 31, 41, 15]
def draw_winning_numbers():
    winning_num = generate_numbers()
    num = randint(1, 45)
    while num in winning_num:
        num = randint(1, 45)
    winning_num.append(num)
    return winning_num


# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):
    count_num = 0
    # 일반 번호 내에서 일치하는 개수 count
    for i in range(len(list2) - 1):
        if list2[i] in list1:
            count_num += 1
    return count_num


# 로또 등수 확인하기
def check(numbers, winning_numbers):
    # length = 보너스 번호 위치
    length = len(winning_numbers) - 1
    match_count = count_matching_numbers(numbers, winning_numbers)
    if match_count == 6:
        award = 1000000000
    elif match_count == 5 and winning_numbers[length] in numbers:
        award = 50000000
    elif match_count == 5:
        award = 1000000
    elif match_count == 4:
        award = 50000
    elif match_count == 3:
        award = 5000
    else:
        award = 0
    return award


lottery = draw_winning_numbers()
user_lottery = generate_numbers()
print(lottery)
print(user_lottery)
print(count_matching_numbers(user_lottery, lottery))
print("%d 원" % check(user_lottery, lottery))