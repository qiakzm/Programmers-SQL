T = int(input())

for _ in range(T):
    # 테스트 케이스
    k = list(map(int, input().split()))
    all_day = []
    # 월일 생성
    for month in range(1, 13):
        # 윤년
        if month == 2:
            days = 29
        # 30일인 달
        elif month in [4, 6, 9, 11]:
            days = 30
        else:
            days = 31
        for day in range(1, days + 1):
            all_day.append(str(month) + str(day))

    for p in range(10):
        if k[p] == 1:
            temp = []
            for d in all_day:
                if str(p) not in d:
                    temp.append(d)
            all_day = temp
                    
    print(len(all_day))