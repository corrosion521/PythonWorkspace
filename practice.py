# from math import *  # math 모듈의 모든 함수, 상수 가져옴
# from random import *
# """
# <숫자 자료형>-----------------------------------------------------------------------------
# """

# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5 + 3)
# print(2 * 8)
# print(3 * (3 + 1))

# """
# <문자형>-----------------------------------------------------------------------------
# """
# print("풍선")
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋㅋ")

# """
# <참/거짓(boolean)>-----------------------------------------------------------------------------
# """
# print(5 > 10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5 > 10))

# """
# <string, numeric, boolean 잇기>-----------------------------------------------------------------------------
# - 애완동물을 소개해 주세요~
# 1. 잇기 :
# 1) + 사용 : 같은 type으로 형변환 필요
# 2) , 사용 : 자동 띄어쓰기 하나 들어감. 다른 data type이어도 이을 수 있음(형변환 필요없음).
# 2. 형변환 :
# 1) ex) str()
# 2) 사용이유 : ex) 문자열에는 문자열만 이을 수 있음.
# """
# name = "연탄이"  # 문자형
# animal = "강아지"  # 문자형
# age = 4  # 숫자 자료형
# hobby = "산책"
# is_adult = age >= 3

# print("우리집 ", animal, "의 이름은 " + name + "예요")
# hobby = "공놀이"
# print(name + "는", age, "살이며," + hobby + "을 아주 좋아해요")
# print(name + "는 어른일까요? "+str(is_adult))


# """
# Quiz) 변수를 이용하여 다음 문장을 출력하시오
# """

# # 변수명 : station
# # 변수 값 : "사당", " 신도림", "인천공항" 순서대로 입력
# # 출력 문장 : xx행 열차가 들어오고 있습니다.

# station = "사당"
# print(station+"행 열차가 들어오고 있습니다.")
# station = "신도림"
# print(station+"행 열차가 들어오고 있습니다.")
# station = "인천공항"
# print(station+"행 열차가 들어오고 있습니다.")


# """
# <연산자>-----------------------------------------------------------------------------
# """
# # 사칙연산
# print(1+1)  # 2
# print(3-2)  # 1
# print(5*2)  # 10
# print(6/3)  # 2

# print(2+3 * 4)  # 14
# print((2+3) * 4)  # 20
# number = 2 + 3 * 4  # 14
# print(number)
# number = number + 2  # 16
# print(number)

# # 할당연산자
# number += 2
# number *= 2
# number -= 2
# number %= 2
# number %= 5
# print(number)

# # 제곱 나머지 몫
# print(2**3)  # 2^3 = 8
# print(5 % 3)  # 나머지 구하기2
# print(10 % 3)  # 1
# print(5//3)  # 1
# print(10//3)  # 3

# # 대소비교
# print(10 > 3)  # True
# print(4 >= 7)  # False
# print(10 < 3)  # False
# print(5 <= 5)  # True

# print(3 == 3)  # True
# print(4 == 2)  # False
# print(3 + 4 == 7)  # True

# # not
# print(1 != 3)  # True
# print(not (1 != 3))  # False

# # and or
# print((3 > 0) and (3 < 5))  # True
# print((3 > 0) & (3 < 5))  # True

# print((3 > 0) or (3 > 5))  # True
# print((3 > 0) | (3 > 5))  # True

# # 삼항 비교
# print(5 > 4 > 3)  # True
# print(5 > 4 > 7)  # False

# '''
#  <함수>------------------------------------------------------------
#  '''
# print(abs(-5))  # 5 , 절대값
# print(pow(4, 2))  # 4^2 = 4*4 = 16 제곱
# print(max(5, 12))  # 12 최대값
# print(min(5, 12))  # 5 최소값
# print(round(3.14))  # 3 반올림
# # math모듈 필요
# print(floor(4.99))  # 내림. 4
# print(ceil(3.14))  # 올림. 4
# print(sqrt(16))  # 제곱근 4
# # 랜덤 함수
# print(random())  # 0.0~1.0미만의 임의의 값 생성
# print(random() * 10)  # 0.0 ~ 10.0미만의 임의의 값 생성
# print(int(random()*10))  # 0~10미만의 임의의 값 생성
# print(int(random()*10)+1)  # 1~10미만의 임의의 값 생성
# print(int(random() * 45)+1)  # 1~45이하의 임의의 값 생성
# print(randrange(1, 45))  # 1~45미만의 임의의 값(정수) 생성
# print(randint(1, 45))  # 1~45이하의 임의의 값(정수) 생성


# '''
# Quiz ) 당신은 코딩 스터디를 새로만들었음.
# 월 4회 스터디 중 3번은 온라인, 1번은 오프라인
# 아래조건에 맞게 오프라인 모임날짜를 정하는 프로그램 작성할 것.

# 조건
# 1. 랜덤
# 2. 월별 날짜는 다름을 감안하여 최소일수인 28이내로 정함
# 3. 매월 1~3일은 스터디 준비를 해야하므로 제외

# (예제)
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.

# ~~
# 설계

# 1. 출력문
# 1) 4~28일 랜덤
# '''

# # 1.1)
# date = (int(random()*28))+1
# # ==
# data = randint(4, 28)

# # 1
# print('오프라인 스터디 모임 날짜는 매월', str(date), '일로 선정되었습니다.')


# """
# <문자열>-----------------------------------------------------------------------------
# """
# # 주석 출력
# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = '파이썬은 쉬워요'
# print(sentence2)
# sentence3 = '''
# 나는 소년이고,
# 파이썬은 쉬워요
# '''
# print(sentence3)

# # 슬라이싱
# jumin = "990120-1234567"
# print("성별 : " + jumin[7])
# print("월 : " + jumin[2:4])
# print("연 : " + jumin[0:2])  # 0 부터 2 직전까지 (0,1)
# print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6])  # 처음부터 6 직전까지
# print("뒤 7자리 : " + jumin[7:])  # 7부터 끝까지
# print("뒤 7자리(뒤에서부터): " + jumin[-7:])  # 7부터 끝까지. 뒤에서부터는 1부터 셈.순서도 주의

# # 함수
# python = 'Python is Amazing'
# print(python.lower())  # 소문자화
# print(python.upper())  # 대문자화
# print(python[0].isupper())  # 대문자인가?
# print(len(python))  # 문자열 길이
# print(python.replace("Python", "Java"))  # 문자열 대체

# index = python.index("n")  # 몇번째인덱스인가
# print(index)  # 5
# index = python.index("n", index+1)  # 몇번째 인덱스인가 그런데, 어디서부터 찾는지
# print(index)  # 15

# print(python.find("Java"))  # 문자열 찾기 . 없으면 -1
# # print(python.index("Java"))  # 인덱스 찾기. 없으면 에러

# print(python.count("n"))  # 몇 번 나왔는가

# # 문자열 포맷
# # (서식문자)
# print("나는 %d살입니다." % 20)  # 숫자
# print("나는 %s을 좋아해요." % "파이썬")  # 문자열
# print("Apple은 %c을 좋아해요." % "A")  # 문자
# print("나는 %s살입니다." % 20)  # %s는 숫자들어가도 출력함
# print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))  # 다중 포맷


# # (중괄호)
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))  # 다중 포맷"
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))  # 다중 포맷- 인덱스
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# # (중괄호-특정 값 기입)
# print("나는 {age}살이며 {color}색을 좋아해요.".format(age=20, color="빨간"))
# print("나는 {age}살이며 {color}색을 좋아해요.".format(color="빨간", age=20))
# print("나는 {age}살이며 {color}색을 좋아해요.".format(color="빨간", age=20))

# # 변수기입
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며 {color}색을 좋아해요.")

# # escape seqence : 프로그램상 표현할 수 없는 것을 표현
# print("백문이 불여일견\n 백견이 불여일타")  # 개행. print문에는 마지막에 개행이 디폴트(end='\n')
# print("저는 \"나도코딩\"입니다.")  # 큰따옴표
# print("저는 \'나도코딩\'입니다.")  # 작은따옴표
# print("c:\\Users\\sky44\\PythonWorkspace>")  # 백슬래시
# print("Red Apple\rPine")  # 커서맨앞+insert기능 PineApple
# print("Redd\bAppple")  # 백스페이스 기능
# print("Red\tApple")  # 탭 기능

# '''
# Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1: http://부분은 제외 => naver.com
# 규칙2: 처음 만나는 점(.)이후 부분은 제외 => naver
# 규칙 3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"
#               (nav)                 (5)          (1)           (!)
# 예) 생성된 비밀번호 : nav51!

# 설계:
# 1. 제거 - replace
# 2. 이후+제거 - slicing
# 3. 출력
# '''

# site = "http://naver.com"
# sidx = site.find('//')+2
# eidx = site.find('.')
# possite = site[sidx:eidx]
# print(possite[0:3]+str(len(possite))+str(site.count('e'))+"!")

# # 답안
# url = "http://naver.com"
# # 1
# my_str = url.replace("http://", "")
# # 2
# my_str = my_str[:my_str.index(".")]  # my_str[0:5]
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e"))+"!"
# # 3
# print("{0} 의 비밀번호는 {1}입니다".format(url, password))

# # <리스트>-----------------------------------------------------------------------------

# # 지하철 칸별로 10명, 20명, 30명
# subway = 10
# subway = 20
# subway = 30
# subway = [10, 20, 30]
# print(subway)

# # 리스트 선언
# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# # 리스트 인덱스
# print(subway.index("조세호"))  # .조세호씨가 몇 번째 칸에 타고있는가?  1

# # append
# subway.append("하하")  # 하하씨가 다음 정류장에서 다음 칸에 탐
# print(subway)

# # insert
# subway.insert(1, "정형돈")  # 정형돈씨를 유재석 / 조세호 사이에 태워봄
# print(subway)

# # pop
# print(subway.pop())  # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄

# # count
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# # 정렬
# num_list = [5, 2, 4, 3, 1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기
# num_list.reverse()
# print(num_list)

# # 모두 삭제
# # num_list.clear()
# # print(num_list)

# # 다양한 자료형 함께 사용
# mix_list = ["조세호", 20, True]
# print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

# # 슬라이싱
# 참조 : [460] practice.py
# print("치킨 당첨자 : {}".format(take[0])) # int형  반환
# print("커피 당첨자 : {}".format(take[1:])) # list형 반환

# # <딕셔너리>-----------------------------------------------------------------------------
# # 키-밸류 사용시

# cabinet = {3: "유재석", 100: "김태호"}
# # 첨자-키
# print(cabinet[3])
# print(cabinet[100])

# # get
# print(cabinet.get(3))

# # 첨자는 없는것 가져오면 에러, get은 None return
# print(cabinet.get(5, "사용가능"))  # 있으면 사용가능
# # print(cabinet[5])
# print("hi")

# # 존재 여부(in)
# print(3 in cabinet)  # True
# print(5 in cabinet)  # False

# cabinet = {"A-3": "유재석", "B-100": "김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# # 딕셔너리 추가 - 그냥 키-밸류 넣기
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# # del- 키(+밸류) 삭제
# del cabinet["A-3"]
# print(cabinet)

# # key만 출력
# print(cabinet.keys())

# # value만 출력
# print(cabinet.values())

# key, value 쌍으로 출력
# print(cabinet.items()) # dict_items([(3, '유재석'), (100, '김태호')])

# # 딕셔너리 삭제
# cabinet.clear()
# print(cabinet)

# for문에서 기본적으로 키가 출력.
# for person in cabinet:
#     print(person)

# # <튜플>-----------------------------------------------------------------------------
# # 리스트와 달리 추가,삭제가 안됨. 속도는 빠름

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# # menu.add("생선까스")

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# # 서로 다른 변수에 값을 한번에 넣기 가능
# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

# # <집합(set)>-----------------------------------------------------------------------------
# # 중복 인식X. 순서 없음

# # 중복 X
# # {} 사용법
# my_set = {1, 2, 3, 3, 3}  # 아무것도 안담고 초기화하면 집합이 아니라 dictionary로 인식함.
# print(my_set)

# # set사용법
# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합 (&, intersaction)
# print(java & python)
# print(java.intersection(python))

# # 합집합 (|, union)
# print(java | python)
# print(java.union(python))

# # 차집합(-, difference)
# print(java - python)
# print(java.difference(python))

# # 추가 add
# python.add("김태호")  # python 할 줄 아는사람이 늘어남
# print(python)

# # 삭제 remove
# python.remove("김태호")
# print(python)

# # <자료구조(list,tuple,dictionary,set)의 변경>-----------------------------------------------------------------------------

# 1)  자료구조간 형변환
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# # set - > 리스트 형변환
# menu = list(menu)

# # ->tuple
# menu = tuple(menu)

# # -> set
# menu = set(menu)

# print(menu, type(menu))

# 2) sample은  리스트 요소 아닌 리스트로 반환
# 아래 퀴즈 참조 (513)

"""
Quiz) 당신의 학교에서는 파이썬 코딩대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20 이라고 가정
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle과 sample을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2,3,4]
-- 축하합니다--

(활용예제)
from random import*
lst = [1,2,3,4,5]
print(lst)
shuffle(lst) # 랜덤 섞임 ex) 5 3 2 4 1
print(lst) #
print(sample(lst,1)) # 랜덤뽑기 4

<내역>
*요약
20C1(커피) + 19C3(치킨) 구현

*해석
1. 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
   편의상 댓글은 20명이 작성하였고, 아이디는 1~20 이라고 가정
   댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
// 20C1(커피) + 19C3(치킨)

~~~
<처리>
*요약
*sample활용한 조합의 구현

*설계
0. from random import*
1. 20개 ID 생성 // 1) for range + set - add
2. 치킨 추첨 // 1) shuffle 2) set-sample 1 +print 3) -
3. 커피 추첨 // 1) shuffle 2)  set - sample 3 + print

~~~

"""

# # 1
# s1 = []
# p1 = set([])
# p2 = set([])

# for i in range(1, 21):
#     s1.append(i)

# # 2
# shuffle(s1)
# chicken = sample(s1, 1)  # 리스트 요소 아닌 리스트로 반환
# p1 = set(s1) - set(chicken)
# print("--당첨자 발표--")
# print("치킨 당첨자 : ", chicken[0])
# # 3
# p1 = list(p1)
# shuffle(p1)
# coffee = sample(p1, 3)
# print("커피 당첨자 : ", coffee)
# print("--축하합니다--\n")

# '''
# ~~~~정답~~~~~~~~~~~~~~~~~~~~~
# # <내역>
# # 요약
# 1. 20C1(커피) + 19C3(치킨)
# # 해석
# 1. 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
#    편의상 댓글은 20명이 작성하였고, 아이디는 1~20 이라고 가정
#    댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# // 20C1(커피) + 19C3(치킨)
# # <처리>
# # 요약
# # 설계
# 1. 20명 리스트 // 1) list + range
# 2. 두 번 뽑는 시행을 한번에  // 1) shuffle 2) sample 3) slicing
# '''
# take = []
# # 1
# users = list(range(1, 21))

# # 2
# # 1)
# shuffle(users)
# # 2)
# take = sample(users, 4)
# # 3)
# print()
# print("--당첨자 발표--")
# print("치킨 당첨자 : {}".format(take[0]))
# print("커피 당첨자 : {}".format(take[1:]))
# print("--축하합니다--\n")

# <조건문>-----------------------------------------------------------------------------

# # if, 입력문
# weather = input("오늘 날씨는 어때요?")  # 입력문
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

# temp = int(input("기온은 어떄요? "))
# if 30 <= temp:
#     print("너무 추워 나가지마")
# elif 10 <= temp and temp < 30:
#     print("ㄱㅊ")
# elif 0 <= temp < 10:  # 파이썬은 이런식으로 쓸 수 있음
#     print("옷 챙겨")
# else:
#     print("나가지마")

# <반복문>-------------------------------------------------------------------------------
# 1. for 문
# in range(0,5)와 같은 출력값(전자는 list형, 후자는 range형)
# for waiting_no in [0, 1, 2, 3, 4]:
#     # {0}이나 {}나 하나뽑을 때는 똑같음 0의 첫번쨰, 1의 첫번째라
#     print("대기번호 : {}".format(waiting_no))

# starbuks = ["아이언맨", "토르", "아이엠그루트"]
# for customer in starbuks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# 2. while문
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0},커피가 준비되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# while True:  # 무한반복
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
#     index += 1

# customer = "토르"
# person = "UnKnown"
# while person != customer:
#     print("{0},커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")

# 3. continue, break
# absent = [2, 5]  # 결석
# no_book = [7]
# for student in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}은 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

# 4. 한 줄 for문
# 출석번호가 1,2,3,4, 앞에 100을 붙이기로함 -> 101,102, 103,104
# students = [1, 2, 3, 4, 5]
# students = [i+100 for i in students]
# print(students)
# 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)
# students = [i.upper()for i in students]  # 대문자 변환
# print(students)

"""
# QUIZ
당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건 1: 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건 2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2 분


#<내역>
#요약
50명 승객에 5~50 랜덤 소요시간 부여 및 카운팅

#해석
50명의 승객과 매칭 기회가 있을 때,승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.// 50명승객 각 5~50 랜덤 소요시간 배정
총 탑승 승객 수를 구하는 프로그램을 작성하시오., 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다. // 50명 승객 중 5~15분 승객만 카운팅

#<처리>
#요약
#설계
1. 50명 승객 소요시간 배정 // list문, [0] - 1번째, 50개의 난수 for문으로 승객 list 생성
2. for문 돌리면서, 5~15인 것만 [O]로 출력
3. 총 탑승 승객 출력
"""
# # 0
# from random import *
# # 1
# guest = [int(random()*50) for i in range(1, 51)]
# # 2
# index = 0
# cnt = 0
# ox = 'O'
# for i in guest:
#     if 5 <= i <= 15:
#         ox = 'O'
#         cnt += 1
#     else:
#         ox = ' '
#     print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(ox, index, i))
#     index += 1
# # 3
# print("총 탑승 승객 :{0}".format(cnt))
# # ~정답~~~~~

# cnt = 0
# for i in range(1, 51):  # 1 ~ 50이라는 수 (승객)
#     time = randrange(5, 51)  # 5분 ~ 50분 소요 시간
#     if 5 <= time <= 15:  # 5분 ~ 15분 이내의 손님, 탑승 수 증가 처리
#         print("[O] {0}번째 손님 (소요시간 : {1}분".format(i, time))
#         cnt += 1
#     else:  # 매칭 실패
#         print("[ ] {0}번째 손님 (소요시간 : {1}분".format(i, time))
# print("총 탑승 승객 :{0}".format(cnt))

# ~개선안~~~
# 차이
# 손님 리스트 for VS 손님 인덱스 for // 후자는 index 변수 만들지 않아도 됨.
# for문 밖 rand VS 안 rand // 이건 전자가 효율적
# 결론 : index변수 X -> for 리스트 + enumerate
# 0
# from random import *
# ride = 'O'
# cnt = 0
# # 1
# guest = [int(random()*50) for i in range(1, 51)]
# # 2
# for i, time in enumerate(guest):
#     if 5 <= time <= 15:
#         ride = 'O'
#         cnt += 1
#     else:
#         ride = ''
#     print("[{2}] {0}번째 손님 (소요시간 : {1}분".format(i, time, ride))
# print("총 탑승 승객 :{0}".format(cnt))

# <함수>-------------------------------------------------------------------------------

# 1. 전달값(parameter)과 반환값(return)
# 1) parameter는 역시 자료형 기입x
# 2) return value는 여러개 반환 가능


# def open_account():
#     print("새로운 계좌가 생성되었습니다.")


# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money


# def withdraw(balance, money):  # 출금
#     if balance >= money:  # 잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money

#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))


# def withdraw_night(balance, money):  # 저녁에 출금
#     commission = 100  # 수수료 100원
#     return commission, balance - money - commission


# balance = 0
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# # balance = withdraw(balance, 500)
# commision, balance = withdraw_night(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commision, balance))

# 2. 기본값 : parameter에 = 디폴트 값을 넣음
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))


# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 수업.


# def profile(name, age=17, main_lang="파이썬"):
#     print("이름  : {0}\t나이 : {1}\t주 사용언어: {2}"
#           .format(name, age, main_lang))


# profile("유재석")
# profile("김태호")

# 3. 키워드 값 : 키워드값(~=)명시하여 argument넣어주면 순서 달리 넣어도 제대로 들어감


# def profile(name, age, main_lang):
#     print(name, age, main_lang)


# profile(name="유재석", main_lang="파이썬", age=20)
# profile(name="유재석", main_lang="파이썬", age=20)


# 4. 가변인자(*args): 위치가변인자.
# 기존
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)
# 가변인자 추가
# def profile(name, age, *language):
#     print("이름 : {0}\t나이: {1}\t".format(name, age))
#     for lang in language:
#         print(lang, end=" ")
#     print()


# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "")

# 5. 지역변수(local) / 전역변수(global) : 함수 내 변수는 local사용. return 유의
# gun = 10  # global

# # func 내 global vs local


# def checkpoint(soldiers):  # 경계근무
#     gun = 20  # local. local변수도 초기화 하지 않으면 에러뜸
#     # global gun  # global
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# # local은 return활용하여 사용


# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 :{0}".format(gun))
#     return gun


# # global
# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))


"""
# ~~QUIZ~~~
표준 체중을 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) x 키(m) x 22
여자 : 키(m) x 키(m) x 21

조건 1 : 표준 체중은 별도의 함수 내에서 계산
    * 함수명 : std_weight
    * 전달값 : 키(height), 성별(gender)
조건 2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.

<내역>
요약: 계산 및 출력 함수 만들기
해석:
1. 표준 체중을 구하는 프로그램을 작성 // 입력값에 대한 출력 프로그램 요청
2. 조건 1 : 표준 체중은 별도의 함수 내에서 계산
    * 함수명 : std_weight
    * 전달값 : 키(height), 성별(gender)
조건 2 : 표준 체중은 소수점 둘째자리까지 표시 // 함수 안에서 계산 및 반올림(둘 째자리)

<처리>
요약: 입력/함수설계/함수호출
설계:
1. 입력 : 키, 성별
2. 함수설계 : // def
1) if 성별
1-1) 키 이용 계산
1-2) 반올림(둘째) // round
3. 함수호출

"""

# # 2


# def calcStdWeight(height, sex):
#     if sex == '남자':
#         stdWeight = round((height*height)*22, 2)
#     elif sex == '여자':
#         stdWeight = round((height*height)*21, 2)
#     return stdWeight


# # 1
# height, sex = input("키와 성별 입력하시오(ex. 175 남자, ex2. 160 여자)").split()

# # 3
# weight = calcStdWeight(int(height)/100, sex)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(
#     height, sex, weight))


# # ~정답~~
# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21


# height = 175
# gender = "남자"
# weight = round(std_weight(height/100, gender), 2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

# # ~차이~
# # 비슷

# <입출력>-------------------------------------------------------------------------------

# 1. 표준 입출력
# 1) sep=' '
# 2) end='\n'생략되어있음
# 3) 표준출력/표준에러
# 4) 정렬 메서드 - ljust(no), rjust(no)
# 5) 형식 출력 메서드 - zfill(no)
# 6) 입력은 항상 숫자던 뭐던 문자열로 받음

# 1),2)
# print("Python", "Java", sep=" ", end="?")
# print("Python", "Java", sep="VS")
# # 3)
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# 4)
# 시험 성적
# scores = {"수학": 0, "영어": 50, "코딩": 100}
# # for subject, score in scores:
# #     print(subject.ljust(8), str(score).rjust(4), sep=":")


# 5)
# 은행 대기 순번표
# 001, 002, 003, ..
# for num in range(1, 21):
#     print("대기번호 : "+str(num).zfill(3))

# 6)
# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 " + answer + "입니다.")
# print(type(answer))

# 2. 출력 포맷
# 1) 정렬
# 2) 음/양
# 3) 빈칸 채우기
# 4) 금액 표기
# 5) 1+2+3+4
# 6) 소수점

# # 1)
# # 빈 자리는 빈공간, 오른쪽 정렬하되, 총 10자리 공간 확보
# print("{0: >10}".format(500))
# # 2) 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 3) 왼쪽 정렬, 빈칸 _로 채움
# print("{0:_<+10}".format(500))
# # 4)
# print("{0:,}".format(100000000000))
# print("{0:+,}".format(100000000000))
# # 5)
# # 3자리마다 콤마, 부호, 자릿수 확보 , 빈자리는 ^
# print("{0:^<+30,}".format(100000000000))
# # 6)
# print("{0:f}".format(5 / 3))
# print("{0:.2f}".format(5 / 3))

# 3. 파일 입출력
# 1) 파일 생성
# 2) 파일 내용 추가
# 3) 파일 읽기

# 1)
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 :0", file=score_file)
# print("영어 :50", file=score_file)
# score_file.close()
# 2)
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()
# 3)
# import pickle
# score_file = open("score.txt", "r", encoding="utf8")
# a. print(score_file.read()) # 파일 전체 읽기
# b.
# print(score_file.readline(), end="")  # 줄별로 읽기, 한 줄 읽고 커서 다음줄로 이동
# print(score_file.readline(), end="")  # 줄별로 읽기, 한 줄 읽고 커서 다음줄로 이동
# print(score_file.readline(), end="")  # 줄별로 읽기, 한 줄 읽고 커서 다음줄로 이동
# print(score_file.readline(), end="")  # 줄별로 읽기, 한 줄 읽고 커서 다음줄로 이동
# score_file.close()
# c. b의 반복문 버전
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()
# d. 리스트로 처리
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")
# score_file.close()

# 4. pickle
# 1) dump(덮어쓰기)
# 2) load(불러오기)
# import pickle

# 1)
# profile_file = open("profile.pickle", "wb")  # 피클은 바이너리(b)로
# profile = {
#     "이름": "박명수",
#     "나이": 30,
#     "취미": ["축구", "골프", "코딩"],
# }  # 저장할 내용
# print(profile)
# pickle.dump(profile, profile_file)  # profile의 정보를 file에 저장
# profile_file.close()

# 2)
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# 5. with : 짧은 라인, close 생략
# 1) pickle - load : pickele 사용시 파일 close하지 않아도됨
# 2) txt - write : 마찬가지
# 3) txt - read : 마찬가지
# import pickle

# # 1)
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))
# # 2)
# with open("study.txt", "w", encoding="utf-8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")
# # 3)
# with open("study.txt", "r", encoding="utf-8") as study_file:
#     print(study_file.read())

"""
# QUIZ
당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- X 주차 주간보고 -
부서 :
이름 :
업무 요약 :

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

조건 : 파일명은 '1주차.txt', '2주차.txt',...와 같이 만듭니다.

<내역>
요약 : X가 다른(X주차 ) 보고서 파일 50개 만들어라
해석 :
1. 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
// 주차 별 (1,2,3..)보고서 파일 생성
2. 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
// 1~50

<처리>
요약 : for문 + file write
설계 :
1. 50주차까지 숫자 달라짐 (제목, 내용의 ~주차) // for 1 ~50
1) 보고서 파일 내용 WRITE // WITH pickle dump
+확인용
2)
"""

# # 1
# for i in range(1, 51):
#     # 1)
#     with open("{0}주차.txt".format(i), "wb") as file:
#         txt = "- {0} 주차 주간보고 -\n부서 :\n이름:\n업무요약:\n".format(i)
#         # print(txt)
#         pickle.dump(txt, file)

# # 2)
# for i in range(1, 51):
#     # 1)
#     with open("{0}주차.txt".format(i), "rb") as file:
#         print(pickle.load(file))
# 정답
# for i in range(1, 51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("-{0} 주차 주간보고 -".format(i))
#         report_file.write("\n부서:")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무 요약:")

# 평가
# 거의 비슷. 내생각엔 문자열에 .format달아주는게 더 편한듯.


# <클래스>-------------------------------------------------------------------------------
# ★  개념
# - 클래스(자동차 설계도), 객체(자동차), 멤버변수(속도, 브랜드), 메서드(주행, 브레이크)
# - 상속(타이어, 엔진), 메서드 오버라이딩(가스차나 전기차 둘다 주행(drive)오버라이딩 )
# 0) 클래스 없이는 객체 생성 시 중복 소스 및 비효율 변수선언 발생(효율성 저하)
# 1) 클래스 선언 - 객체 생성
# a. 클래스 paramater만큼 객체 생성시 argument 값 필요
# 2) 멤버변수 외부 접근 가능
# a. 외부에서 객체의 멤버변수 확장 가능
# 3) 메소드
# 4) 상속 : class par에 넣음. 타 클래스의 멤버변수, 메소드를 받음 (받는 쪽은 자식클래스, 그 역은 부모클래스)
# 5) 다중상속 : 여러 부모클래스를 상속받음.
# ex) Unit <- AttackUnit, Flyable.     AttackUnit, Flyabnle <- FlyableAttackUnit
# 6) 메서드 오버라이드
# ex) Unit(move) <- AttackUnit, Flyable.     AttackUnit, Flyabnle <- FlyableAttackUnit(move 재정의)
# 7) pass : 아무것도 안함.예비 공간
# 8) super :
# a) self사용안하고 부모클래스 지시 가능
# b) 단, 다중 상속일 경우는 지양(첫번째 인자만 지시 가능)
# 9) 유닛 추가 - 총 유닛수 7개 실질적인 개체는 마린, 탱크, 레이스
# 10) 게임
# a) isinstance : 해당 객체가 그 클래스가맞는지

# # 0)
# # 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# # 비효율 변수
# name = "마린"  # 유닛의 이름
# hp = 40  # 유닛의 체력
# damage = 5  # 유닛의 공격력
# # 중복 소스
# print("{0} 유닛이 생성되었습니다".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수  있는데, 일반모드 / 시즈모드.
# # 비효율 변수
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
# # 중복 소스
# print("{0} 유닛이 생성되었습니다".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))


# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(
#         name, location, damage))


# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# tank2_name = "탱크2"
# tank2_hp = 150
# tank2_damage = 35
# # 중복 소스
# print("{0} 유닛이 생성되었습니다".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))
# attack(tank_name, "1시", tank2_damage)

# # 1)
# # 일반 유닛
# from random import *
# class Unit:
#     def __init__(self, name, hp, speed):  # a)
#         self.name = name  # 멤버변수 : self.name, hp, ..
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다".format(name))

#     def move(self, location):
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(
#             self.name, location, self.speed))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))


# # marine1 = Unit("마린", 40, 5)
# # marine2 = Unit("마린", 40, 5)
# # tank1 = Unit("탱크", 150, 35)

# # # 2)
# # # 레이스 : 공중유닛, 비행기. 클로킹(상대방에게 보이지 않음)
# # wraith1 = Unit("레이스", 80, 5)
# # print("유닛 이름 :{0}, 공격력 :{1}".format(wraith1.name, wraith1.damage))

# # # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# # wraith2 = Unit("레이스", 80, 5)
# # # a.
# # wraith2.clocking = True

# # if wraith2.clocking == True:
# #     print("{0} 는 현재 클로킹 상대입니다.".format(wraith2.name))

# # # 에러 발생
# # if wraith1.clocking == True:
# #     print("{0} 는 현재 클로킹 상대입니다.".format(wraith2.name))

# # 3)
# # 4)
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         # 4)
#         # self.name = name
#         # self.hp = hp
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(
#             self.name, location, self.damage))


# # # 파이어뱃 : 공격 유닛, 화염방사기.
# # firebat1 = AttackUnit("파이어뱃", 50, 16)
# # firebat1.attack("5시")

# # # 공격 2번 받는다고 가정
# # firebat1.damaged(25)
# # firebat1.damaged(25)


# # 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃/ 탱크 등을 수송. 공격 X
# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

# #    메소드 오버라이딩
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(
#             name, location, self.flying_speed))

# # 5)
# # 공중 공격 유닛 클래스


# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 speed 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         self.fly(self.name, location)


# # # 발키리 : 공중 공격 유닛, 한 번에 14발 미사일 발사
# # valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# # valkyrie.fly(valkyrie.name, "3시")


# # # 6)
# # # 벌쳐 : 지상유닛, 기동성이 좋음.
# # vulture = AttackUnit("벌쳐", 80, 10, 20)

# # # 배틀 크루저 : 공중 유닛, 체력 높고 공격력 높음
# # battlecruiser = FlyableAttackUnit("배틀 크루저", 500, 25, 3)

# # # 매번 지상유닛인지 공중유닛인지 확인하고 그에 따라 move, fly를 써야하는 불편함이 있음
# # # vulture.move("11시")
# # # battlecruiser.fly(battlecruiser.name, "9시")

# # # 메소드 오버로딩 후
# # vulture.move("11시")
# # battlecruiser.move("9시")  # 공중유닛이동이 지상유닛 이동을 덮어씀(override)

# # # 7)
# # class BuildingUnit(Unit):
# #     def __init__(self, name, hp, location):
# #         pass


# # # 서플라이 디폿 : 건물, 1개 건물 = 8유닛.
# # supplay_depot = BuildingUnit("서플라이 디폿", 500, "7시")


# # def game_start():
# #     print("[알림] 새로운 게임을 시작합니다.")


# # def game_over():
# #     pass


# # game_start()
# # game_over()

# # 8)
# # class BuildingUnit(Unit):
# #     def __init__(self, name, hp, location):
# #         # Unit.__init__(name, hp, 0) #a)
# #         super().__init(name, hp, 0)
# #         self.location = location

# # # b)

# # ~ 테스트 유닛
# # class Unit:
# #     def __init__(self):
# #         print("Unit 생성자")


# # class Flyable:
# #     def __init__(self):
# #         print("Flyable 생성자")


# # class FlyableUnit(Flyable, Unit):
# #     def __init__(self):
# #         Unit.__init__(self)
# #         Flyable.__init__(self)


# # # 드랍쉽
# # dropship = FlyableUnit()

# # 마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)
#     # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10감소

#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다. (hp 10감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))

# # 탱크


# class Tank(AttackUnit):
#     # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
#     seize_developed = False  # 시즈모드 개발 여부

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return
#         # 현재 시즈모드가 아닐 때 -> 시즈모드
#         if self.seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True
#         # 현재 시즈모드일 때 -> 해제
#         else:
#             print("{0} : 시즈모드로 해제합니다".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False


# # 레이스


# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False  # 클로킹 모드 (해제 상태)

#     def clocking(self):
#         if self.clocked == True:  # 클로킹 모드 -> 모드 해제
#             print("{0} : 클로킹 모드 해제합니다".format(self.name))
#         else:  # 클로킹 모드 해제-> 모드 설정
#             print("{0} : 클로킹 모드 설정 합니다".format(self.name))
#             self.clocked = True


# # 10)


# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")


# def game_over():
#     print("Player : gg")
#     print("[Player] 님이 게임에서 퇴장하셨습니다.")


# # 실제 게임 진행
# game_start()

# # 마린 3기 생성
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# # 탱크 2기 생성
# t1 = Tank()
# t2 = Tank()

# # 레이스 1기 생성
# w1 = Wraith()

# # 유닛 일괄 관리
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")

# # 탱크 시즈모드 개발
# Tank.seize_developed = True
# print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

# # 공격 모드 중비 (마린 : 스팀팩, 탱크 : 시즈모드 , 레이스 : 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()
# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")

# # 전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5, 21))  # 공격은 랜덤으로 받음 (5~20)

# # 게임 종료
# game_over()

"""
# QUIZ
주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

(출력 예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년

- 내역
    - 요약 : 클래스 코드 작성하여 출력
    - 해석
- 처리
    - 요약
    - 설계:
        1. parameter이용하여 매물 초기화에 대입
        2. 매물 정보 표시에서 멤버변수 이용하여 출력
        1) 월세만 형식 다름-조건문+ 튜플
        3. 인스턴스화 및 매물 정보 표시
        4. 인스턴스 담아 반복문 출력
"""

# [코드]


# class House:
#     # 매물 초기화,#1
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     # 매물 정보 표시,#2
#     def show_detail(self):
#         # 1)
#         if self.deal_type == "월세":
#             print(
#                 "{0} {1} {2} {3}/{4} {5}년".format(
#                     self.location,
#                     self.house_type,
#                     self.deal_type,
#                     self.price[0],
#                     self.price[1],
#                     self.completion_year,
#                 )
#             )
#         else:
#             print(
#                 "{0} {1} {2} {3} {4}년".format(
#                     self.location,
#                     self.house_type,
#                     self.deal_type,
#                     self.price,
#                     self.completion_year,
#                 )
#             )


# # 3
# s1 = House("강남", "아파트", "매매", "10억", 2010)
# s2 = House("마포", "오피스텔", "전세", "5억", 2010)
# s3 = House("송파", "빌라", "월세", [500, 50], 2010)

# # 4
# all = []
# all.append(s1)
# all.append(s2)
# all.append(s3)

# print("총 {0}대의 매물이 있습니다.".format(len(all)))

# for sale in all:
#     sale.show_detail()

# 정답과 거의 유사함.

# <예외처리>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1.예외처리 (try~exept):
# 1) 에러잡고 분기처리.
# 2) 에러는 여러가지임(ValueError, IndexError, ZeroDivisionError 등..).
# 3) Exception에 에러가 들어감
# 2. 에러 발생시키기(raise) : 조건에 따른 에러 발생시키기
# 3. 사용자 정의 예외처리 : class 기반 std 에러
# 1) __str__ 메서드 : 클래스 객체 출력시 어떤 문자열로 표현될지 정의.
# 4. finally : 예외처리문(try~except)에서 무조건 실행(에러 발생 시에도 실행됨)


# 1.
# 1)
# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:  # 2)
#     print("에러! 잘못된 값을 입력했습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:  # 3)
#     print("에러! : {0}".format(err))


# # # 3.
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     # 3.1)
#     def __str__(self):
#         return self.msg


# # 2.
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         # raise ValueError
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))  # 3.
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력했습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)  # 3.1)
# finally:  # 4
#     print("계산기를 이용해 주셔서 감사합니다.")


"""
<QUIZ>
동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

조건 1: 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
        출력 메시지 : "잘못된 값을 입력하였습니다."
조건 2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
        치킨 소진 시 사용자 정의 에러[SoldOutError]주문을 발생시키고 프로그램 종료
        출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

- 내역
    - 요약 : 예외처리문 추가
    - 해석 :
        1. 적절한 예외처리 구문을 넣으시오.// try~except염두
        2. 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리 // std err
        3. 치킨 소진 시 사용자 정의 에러[SoldOutError]주문을 발생시키고 프로그램 종료 // cbo err 설계. break
- 처리
    - 요약
    - 설계
        1. 반복문 안 try~except
        2. 조건문 (1<) raise ValueError
        3. cbo err 설계(par - chicken) 및 chiken == 0 -> raise err
"""


# 2
# class SoldOutError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg


# chicken = 10
# waiting = 1  # 홀 안에는 현재 만석. 대기번호 1부터 시작.
# while True:
#     # 1
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken:  # 남은 치킨보다 주문량이 많을때
#             print("재료가 부족합니다.")
#         elif order <= 0:  # 2
#             raise ValueError
#         else:
#             print(
#                 "[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order)
#             )
#             waiting += 1
#             chicken -= order
#         # 3
#         if chicken == 0:
#             raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")  # 2
#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError as err:
#         print(err)
#         break

# # 정답비교 : 비슷은 하나, 문제 해석이 잘못됨(재료 소진 및 글자 자체를 제대로 안읽음)

# <모듈과 패키지>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1. 모듈 : ex) 자동차의 타이어 마모시 타이어만 교체. 부품만 교체가능하면 유지보수,재사용 쉬움
# 1) 확장자 : .py
# 2) 파이썬 기준 : 함수정의 , 클래스 담음
# 3) import 방식
# a) 모듈.
# b) 그냥 / / from~import 사용시, 모듈 내 클래스 메서드(ex. from travel.thailand import ThailandPackage)사용 가능
# c) alias
# d) 모듈 내 특정 함수만
# e) d)인데 거기에 alis - price지만 price함수가 아니라, price_soldier임.
# 2. 패키지 : 모듈을 담는 파일(thailand, vietnam 등 모듈을 담는 travel 패키지)
# 1) 1-3-b 참조
# 3. __all__ : 특정 모듈만 정의할 수 있음
# 4. 모듈 직접 실행(__name__ == "__main__") : 모듈내에서 매직메소드(__name~~)를 사용하여,
#  모듈파일 직접실행하는경우, 외부호출하는 경우에 대해 분기를 설정할 수 있다.
# 5. 패키지, 모듈 위치(inspect-getfile) : 파이썬 라이브러리 모듈인지, 사용자 생성 모듈인지 등 위치 파악 가능
# 6. pip install (패키지 설치) : 딴 사람거 가져다 쓰기 (ex. pypi.org). 터미널에 pip install~입력
# 1) 설치 : pip install beautifulsoup4
# 2) 버전, 패키지 리스트 : pip list
# 3) 정보 : pip show beautifulsoup4
# 4) 최신화 : pip install --upgrade beautifulsoup4
# 5) 삭제 : pip uninstall beautifulsoup4
# 7. 내장함수 : 따로 import 할 필요없이 사용가능한 함수 (ex. input, dir, pickle)
# 1) dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
#          외장함수는 import했을 때 하나씩 추가됨을 확인 가능
# 2) 모듈객체(random), 변수객체 등에서 사용가능한 내장함수 파악 가능.
# 3) "내장함수" "https://docs.python.org/3/library/functions.html"
# 7. 외장함수 : 따로 import 할 필요없이 사용가능한 함수 (ex. random)
# 1) glob : 경로 내 폴더/ 파일 목록 조회(윈도우 dir). practic.py안 py파일 다 보여줌
# 2) os : 운영체제에서 제공하는 기본 기능
# 3) time : 시간관련 함수
# 4) datetime : 날짜 관련 함수
# 5) time delta : 날짜 사이 간격

# 1.
# from theater_module import price, price_morning # d)
# from theater_module import * # b)
# import theater_module  # 3-a
# import theater_module as mv # c)

# theater_module.price(3)  # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4)  # 4명이서 조조 할인 영화 보러 갔을 때
# theater_module.price_soldier(5)  # 5명이서 군인 할인 영화 보러 갔을 때

# mv.price_morning(3)

# price(3)
# price_morning(4)
# price_morning(5)

# from theater_module import price_soldier as price # e)
# price(5)

# 2.

# import travel. thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# 3.
# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()
# # 안됨 not defined. init.py에서 vietnam 모듈만 정의하기에
# trip_to2 = thailand.ThailandPackage()

# 4.
# thailand.py에서 직접실행
# practice 실행
# from travel import thailand
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# 5.
# from travel import thailand
# import inspect
# import random

# # ~ sky44\AppData\Local\Programs\Python\Python38\lib\random.py
# print(inspect.getfile(random))
# # ~sky44\OneDrive\바탕 화면\정지오\PythonWorkspace\travel\thailand.py
# print(inspect.getfile(thailand))

# 6.
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# 7.

# 1)
# print(dir())
# import random
# print(dir())
# import pickle
# print(dir())

# # 2)
# print(dir(random))
# lst = [1, 2, 3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))

# # 1)
# import glob
# print(glob.glob("*.py"))

# 2)
# import os
# print(os.getcwd) # 현 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())

# 3)
# import datetime
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# # 4)
# print("오늘 날짜는", datetime.date.today())

# # 5)
# today = datetime.date.today()  # 오늘 날짜저장
# td = datetime.timedelta(days=100)  # 100일 저장
# print("우리가 만난지 100일은", today+td)  # 오늘부터 100일후

'''
<Quiz>
프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

조건 : 모듈 파일명은 byme.py로 작성

(모듈 사용 예제)
import byme
byme.sign()

(출력 예제)
이 프로그램은 나도 코딩에 의해 만들어졌습니다.
유튜브 : http://youtube.com
이메일 : nadocoding@gmail.com

- 내역
    - 요약 : 모듈만들어서 사용해봐라
- 처리
    - 요약 : 모듈에 외장함수 만들어서 사용
    - 설계 :
        1. byme.py 모듈 생성
        2. 모듈 내 sign 메서드 생성 및 출력문 넣기
        3. import 및 실행
'''

# 3)
# 4)
import bymee
bymee.sign()