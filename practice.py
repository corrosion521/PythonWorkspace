from math import *  # math 모듈의 모든 함수, 상수 가져옴
from random import *
"""
<숫자 자료형>-----------------------------------------------------------------------------
"""

print(5)
print(-10)
print(3.14)
print(1000)
print(5 + 3)
print(2 * 8)
print(3 * (3 + 1))

"""
<문자형>-----------------------------------------------------------------------------
"""
print("풍선")
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋ")

"""
<참/거짓(boolean)>-----------------------------------------------------------------------------
"""
print(5 > 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

"""
<string, numeric, boolean 잇기>-----------------------------------------------------------------------------
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
<연산자>-----------------------------------------------------------------------------
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

'''
 <함수>------------------------------------------------------------
 '''
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


'''
Quiz ) 당신은 코딩 스터디를 새로만들었음.
월 4회 스터디 중 3번은 온라인, 1번은 오프라인
아래조건에 맞게 오프라인 모임날짜를 정하는 프로그램 작성할 것.

조건
1. 랜덤
2. 월별 날짜는 다름을 감안하여 최소일수인 28이내로 정함
3. 매월 1~3일은 스터디 준비를 해야하므로 제외

(예제)
오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.

~~
설계

1. 출력문
1) 4~28일 랜덤 
'''

# 1.1)
date = (int(random()*28))+1
# ==
data = randint(4, 28)

# 1
print('오프라인 스터디 모임 날짜는 매월', str(date), '일로 선정되었습니다.')


"""
<문자열>-----------------------------------------------------------------------------
"""
# 주석 출력
sentence = '나는 소년입니다'
print(sentence)
sentence2 = '파이썬은 쉬워요'
print(sentence2)
sentence3 = '''
나는 소년이고,
파이썬은 쉬워요
'''
print(sentence3)

# 슬라이싱
jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("월 : " + jumin[2:4])
print("연 : " + jumin[0:2])  # 0 부터 2 직전까지 (0,1)
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])  # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:])  # 7부터 끝까지
print("뒤 7자리(뒤에서부터): " + jumin[-7:])  # 7부터 끝까지. 뒤에서부터는 1부터 셈.순서도 주의

# 함수
python = 'Python is Amazing'
print(python.lower())  # 소문자화
print(python.upper())  # 대문자화
print(python[0].isupper())  # 대문자인가?
print(len(python))  # 문자열 길이
print(python.replace("Python", "Java"))  # 문자열 대체

index = python.index("n")  # 몇번째인덱스인가
print(index)  # 5
index = python.index("n", index+1)  # 몇번째 인덱스인가 그런데, 어디서부터 찾는지
print(index)  # 15

print(python.find("Java"))  # 문자열 찾기 . 없으면 -1
# print(python.index("Java"))  # 인덱스 찾기. 없으면 에러

print(python.count("n"))  # 몇 번 나왔는가

# 문자열 포맷
print("나는 %d살입니다." % 20)  # 서식문자
print("나는 %s을 좋아해요." % "파이썬")
