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
# (서식문자)
print("나는 %d살입니다." % 20)  # 숫자
print("나는 %s을 좋아해요." % "파이썬")  # 문자열
print("Apple은 %c을 좋아해요." % "A")  # 문자
print("나는 %s살입니다." % 20)  # %s는 숫자들어가도 출력함
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))  # 다중 포맷


# (중괄호)
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))  # 다중 포맷"
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))  # 다중 포맷- 인덱스
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# (중괄호-특정 값 기입)
print("나는 {age}살이며 {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며 {color}색을 좋아해요.".format(color="빨간", age=20))
print("나는 {age}살이며 {color}색을 좋아해요.".format(color="빨간", age=20))

# 변수기입
age = 20
color = "빨간"
print(f"나는 {age}살이며 {color}색을 좋아해요.")

# escape seqence : 프로그램상 표현할 수 없는 것을 표현
print("백문이 불여일견\n 백견이 불여일타")  # 개행
print("저는 \"나도코딩\"입니다.")  # 큰따옴표
print("저는 \'나도코딩\'입니다.")  # 작은따옴표
print("c:\\Users\\sky44\\PythonWorkspace>")  # 백슬래시
print("Red Apple\rPine")  # 커서맨앞+insert기능 PineApple
print("Redd\bAppple")  # 백스페이스 기능
print("Red\tApple")  # 탭 기능

'''
Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

예) http://naver.com
규칙1: http://부분은 제외 => naver.com
규칙2: 처음 만나는 점(.)이후 부분은 제외 => naver
규칙 3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"
              (nav)                 (5)          (1)           (!)
예) 생성된 비밀번호 : nav51!

설계:
1. 제거 - replace
2. 이후+제거 - slicing
3. 출력
'''

site = "http://naver.com"
sidx = site.find('//')+2
eidx = site.find('.')
possite = site[sidx:eidx]
print(possite[0:3]+str(len(possite))+str(site.count('e'))+"!")

# 답안
url = "http://naver.com"
# 1
my_str = url.replace("http://", "")
# 2
my_str = my_str[:my_str.index(".")]  # my_str[0:5]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e"))+"!"
# 3
print("{0} 의 비밀번호는 {1}입니다".format(url, password))

# <리스트>-----------------------------------------------------------------------------

# 지하철 칸별로 10명, 20명, 30명
subway = 10
subway = 20
subway = 30
subway = [10, 20, 30]
print(subway)

# 리스트 선언
subway = ["유재석", "조세호", "박명수"]
print(subway)

# 리스트 인덱스
print(subway.index("조세호"))  # .조세호씨가 몇 번째 칸에 타고있는가?  1

# append
subway.append("하하")  # 하하씨가 다음 정류장에서 다음 칸에 탐
print(subway)

# insert
subway.insert(1, "정형돈")  # 정형돈씨를 유재석 / 조세호 사이에 태워봄
print(subway)

# pop
print(subway.pop())  # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄

# count
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 삭제
# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

# <딕셔너리>-----------------------------------------------------------------------------
# 키-밸류 사용시

cabinet = {3: "유재석", 100: "김태호"}
# 첨자-키
print(cabinet[3])
print(cabinet[100])

# get
print(cabinet.get(3))

# 첨자는 없는것 가져오면 에러, get은 None return
print(cabinet.get(5, "사용가능"))  # 있으면 사용가능
# print(cabinet[5])
print("hi")

# 존재 여부(in)
print(3 in cabinet)  # True
print(5 in cabinet)  # False

cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 딕셔너리 추가 - 그냥 키-밸류 넣기
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# del- 키(+밸류) 삭제
del cabinet["A-3"]
print(cabinet)

# key만 출력
print(cabinet.keys())

# value만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 딕셔너리 삭제
cabinet.clear()
print(cabinet)

# <튜플>-----------------------------------------------------------------------------
# 리스트와 달리 추가,삭제가 안됨. 속도는 빠름

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스")

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

# 서로 다른 변수에 값을 한번에 넣기 가능
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

# <집합(set)>-----------------------------------------------------------------------------
# 중복 인식X. 순서 없음

# 중복 X
# {} 사용법
my_set = {1, 2, 3, 3, 3}
print(my_set)

# set사용법
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (&, intersaction)
print(java & python)
print(java.intersection(python))

# 합집합 (|, union)
print(java | python)
print(java.union(python))

# 차집합(-, difference)
print(java - python)
print(java.difference(python))

# 추가 add
python.add("김태호")  # python 할 줄 아는사람이 늘어남
print(python)

# 삭제 remove
python.remove("김태호")
print(python)

# <자료구조(list,tuple,dictionary,set)의 변경>-----------------------------------------------------------------------------

menu = {"커피", "우유", "주스"}
print(menu, type(menu))

# set - > 리스트 형변환
menu = list(menu)

# ->tuple
menu = tuple(menu)

# -> set
menu = set(menu)

print(menu, type(menu))
