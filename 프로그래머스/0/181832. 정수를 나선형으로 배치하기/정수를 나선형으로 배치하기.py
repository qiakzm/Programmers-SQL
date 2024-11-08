# 초기 방향 설정이 중요하다. 숫자 기입의 진행 방향이 우 -> 하 -> 좌 -> 상 -> 우
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 순서대로 우, 하, 좌, 상

def solution(n):
    answer = [[0] * n for _ in range(n)]
    x, y = 0, 0
    c = 1
    dt = 0
    
    while c <= n * n: # c가 나올 수 있는 최고 숫자 전까지 진행
        answer[x][y] = c # 첫 0,0은 1부터 시작
        c += 1 # c가 기입되고 1증가
        xx, yy = x + direction[dt][0], y + direction[dt][1] # 다음 방향 설정
        if 0 <= xx < n and 0 <= yy < n: # x와 y 모두 끝에 달하지 않았을 때
            if answer[xx][yy] != 0: # 그리고 0이 아닐 경우 = 기입이 돼 있을 경우
                dt = (dt + 1) % 4   # dt 초기화
                x, y = x + direction[dt][0], y + direction[dt][1] # 방향 설정
            else:
                x, y = xx, yy # [x][y]가 0일 때, 다시 while문 상단으로 올라가 기입
        else:   # x혹은 y가 끝에 도달했을 때
            dt = (dt + 1) % 4   # dt 초기화
            x, y = x + direction[dt][0], y + direction[dt][1] # 방향 재설정
    return answer