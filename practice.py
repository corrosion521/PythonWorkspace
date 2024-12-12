from math import *  # math 모듈의 모든 함수, 상수 가져옴
from random import *
"""
<숫자 자료형>
"""

print(5)
print(-10)
print(3.14)
print(1000)
print(5 + 3)
print(2 * 8)
print(3 * (3 + 1))

"""
<문자형>
"""
print("풍선")
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋ")

"""
<참/거짓(boolean)>
"""
print(5 > 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

"""
<string, numeric, boolean 잇기>
- 애완동물을 소개해 주세요~
1. 잇기 : 
1) + 사용 : 같은 type으로 형변환 필요
2) , 사용 : 자동 띄어쓰기 하나 들어감. 다른 data type이어도 이을 수 있음(형변환 필요없음). 
2. 형변환 : 
1) ex) str()
2) 사용이유 : ex) 문자열에는 문자열만 이을 수 있음.  
"""
name = "연탄이"  # 문자형
animal = "강아지"  # 문자형
age = 4  # 숫자 자료형
hobby = "산책"
is_adult = age >= 3

print("우리집 ", animal, "의 이름은 " + name + "예요")
hobby = "공놀이"
print(name + "는", age, "살이며," + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? "+str(is_adult))


"""
Quiz) 변수를 이용하여 다음 문장을 출력하시오
"""

# 변수명 : station
# 변수 값 : "사당", " 신도림", "인천공항" 순서대로 입력
# 출력 문장 : xx행 열차가 들어오고 있습니다.

station = "사당"
print(station+"행 열차가 들어오고 있습니다.")
station = "신도림"
print(station+"행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station+"행 열차가 들어오고 있습니다.")


"""
<연산자>
"""
# 사칙연산
print(1+1)  # 2
print(3-2)  # 1
print(5*2)  # 10
print(6/3)  # 2

print(2+3 * 4)  # 14
print((2+3) * 4)  # 20
number = 2 + 3 * 4  # 14
print(number)
number = number + 2  # 16
print(number)

# 할당연산자
number += 2
number *= 2
number -= 2
number %= 2
number %= 5
print(number)

# 제곱 나머지 몫
print(2**3)  # 2^3 = 8
print(5 % 3)  # 나머지 구하기2
print(10 % 3)  # 1
print(5//3)  # 1
print(10//3)  # 3

# 대소비교
print(10 > 3)  # True
print(4 >= 7)  # False
print(10 < 3)  # False
print(5 <= 5)  # True

print(3 == 3)  # True
print(4 == 2)  # False
print(3 + 4 == 7)  # True

# not
print(1 != 3)  # True
print(not (1 != 3))  # False

# and or
print((3 > 0) and (3 < 5))  # True
print((3 > 0) & (3 < 5))  # True

print((3 > 0) or (3 > 5))  # True
print((3 > 0) | (3 > 5))  # True

# 삼항 비교
print(5 > 4 > 3)  # True
print(5 > 4 > 7)  # False

# <함수>
print(abs(-5))  # 5 , 절대값
print(pow(4, 2))  # 4^2 = 4*4 = 16 제곱
print(max(5, 12))  # 12 최대값
print(min(5, 12))  # 5 최소값
print(round(3.14))  # 3 반올림
# math모듈 필요
print(floor(4.99))  # 내림. 4
print(ceil(3.14))  # 올림. 4
print(sqrt(16))  # 제곱근 4
# 랜덤 함수
print(random())  # 0.0~1.0미만의 임의의 값 생성
print(random() * 10)  # 0.0 ~ 10.0미만의 임의의 값 생성
print(int(random()*10))  # 0~10미만의 임의의 값 생성
print(int(random()*10)+1)  # 1~10미만의 임의의 값 생성
print(int(random() * 45)+1)  # 1~45이하의 임의의 값 생성
print(randrange(1, 45))  # 1~45미만의 임의의 값(정수) 생성
print(randint(1, 45))  # 1~45이하의 임의의 값(정수) 생성
