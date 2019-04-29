from random import randint

#기회
tries = 4

#시도한 횟수
count = 0

#랜덤 수
ANSWER = randint(1, 20)

#숫자 맞추기
while tries > 0:
    guess = int(input("기회가 %d번 남았습니다. 1-20사이의 숫자를 맞춰보세요: " % (tries)))

    if guess > ANSWER:
        print("DOWN")
        count += 1
    elif guess < ANSWER:
        print("UP")
        count += 1
    elif guess == ANSWER:
        count += 1
        print("축하합니다. %d번만에 숫자를 맞추셨습니다." % (count))
        break

    tries -= 1

if tries == 0:
    print("아쉽습니다. 정답은 %d였습니다." % (ANSWER))
