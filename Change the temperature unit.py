i = 0

# 화씨 온도에서 섭씨 온도로 바꿔주는 함수
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
    # 코드를 입력하세요.

# 테스트용 온도 리스트
sample_temperature_list = [40, 15, 32, 64, -4, 11]

# 화씨 온도 출력
print("화씨 온도 리스트: " + str(sample_temperature_list))

# 리스트의 값들을 화씨에서 섭씨로 변환
# 코드를 입력하세요.
while i < len(sample_temperature_list):
    sample_temperature_list[i] = fahrenheit_to_celsius(sample_temperature_list[i])
    i += 1

# 섭씨 온도 출력
print("섭씨 온도 리스트: " + str(sample_temperature_list))