- 구현
1. for문으로 데이터 추가(ex. append, add)하지 않고 range만으로 가능
    - 참조 : [490] practice.py
    - ex) users = range(1, 20)  # 이대로면 users가 range타입임
    - ex) users = list(users)  # range
2. 반복 행위(ex. 조합 - 20C1 + 19C3)처럼 보이는 것을 갇단히 구현할 수 있는지 확인
    - 참조 : [490] practice.py
    - ex) shuffle(users) , winners = sample(users, 4)  # 4명중 1명은 치킨, 3명은 커피
    