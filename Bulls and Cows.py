from random import randint

baseball = []

while len(baseball) < 3:
    new_baseball = randint(0, 9)
    while new_baseball in baseball:
        new_baseball = randint(0, 9)
    baseball.append(new_baseball)

count = 0
# strike
s = 0

print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")

while s < 3:
    # 스트라이크 개수 초기화
    s = 0
    # 볼 개수 초기화 및 선언
    b = 0
    # answer_list 의 index 지정
    index = 0

    # 사용자가 입력하는 숫자를 넣을 리스트
    answer_list = []

    print("")
    print("세 수를 하나씩 차례대로 입력하세요.")
    count += 1

    # 숫자 입력 받기 및 각 숫자에 대한 유효성 확인
    while len(answer_list) < 3:
        new_answer_list = int(input("%d번째 수를 입력하세요: " % (len(answer_list) + 1)))
        if new_answer_list in answer_list:
            print("중복되는 수 입니다. 다시 입력해주세요.")
        elif new_answer_list >= 10 or new_answer_list < 0:
            print("범위를 벗어나는 수 입니다. 다시 입력해주세요.")
        else:
            answer_list.append(new_answer_list)

    while index < 3:
        if baseball[index] == answer_list[index]:
            s += 1
        elif (answer_list[index] in baseball) == 1:
            b += 1
        index += 1
    print("%dS %dB" % (s, b))

print("축하합니다. %d번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % count)
