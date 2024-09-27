for _ in range(2):
    scores = 0
    T, F, S, P, C = map(int, input().split())
    scores = T*6 + F*3 + S*2 + P*1 + C*2
    print(scores, end = ' ')