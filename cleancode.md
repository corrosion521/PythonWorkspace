1. 가독성 : 직관적작명, 개행  
   1. 반복문 첨자([]) 대신에 enumerate
    - 참조 : [721] practice.py
    - ex) 기능은 같지만 가독성문제(첨자는 for i in len(list),[] 등..)
2. 효율성 : 연산 최소화 
   1. for문으로 데이터 추가(ex. append, add)하지 않고 range만으로 가능
    - 참조 : [490] practice.py
    - ex) users = range(1, 20)  # 이대로면 users가 range타입임
    - ex) users = list(users)  # range
   2. 반복 행위(ex. 조합 - 20C1 + 19C3)처럼 보이는 것을 간단히 구현할 수 있는지 확인
       - 참조 : [490] practice.py
       - ex) shuffle(users) , winners = sample(users, 4)  # 4명중 1명은 치킨, 3명은 커피
   3. 클래스 사용하여 객체 생성 시 중복 소스 및 비효율 선언 제거
        - 참조 : [1104] practice.py
        - ex) 반복 객체 생성시 클래스 생성
3. 안정성 : 기존 코드 흐름 파악 후 최소한 수정(잔머리)


