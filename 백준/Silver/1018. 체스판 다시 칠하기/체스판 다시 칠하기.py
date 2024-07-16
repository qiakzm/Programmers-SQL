M, N = map(int, input().split())
board = []
for _ in range(M):
    k = input()
    board.append(k)
answer = []

for i in range(M-7):
    for j in range(N-7):
        first_w = 0
        first_b = 0
        
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0: # 짝수일 때,
                    if board[k][l] != 'W':
                        first_w += 1
                    if board[k][l] != 'B':
                        first_b += 1
                else: #홀수일 때
                    if board[k][l] != 'B':
                        first_w += 1
                    if board[k][l] != 'W':
                        first_b += 1
        answer.append(first_w)
        answer.append(first_b)
        
print(min(answer))