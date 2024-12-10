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
