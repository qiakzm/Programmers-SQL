N = int(input())
permut = list(map(int, input().split()))

if permut == sorted(permut):
    print(-1)
else:
    # 뒤에서 처음 증가하는 부분이 있는가
    for i in range(N-1, 0, -1):
        if permut[i-1] > permut[i]:
            break
    for j in range(N-1, 0, -1):
        if permut[i-1] > permut[j]:
            # 둘이 바꿔주고
            permut[i-1], permut[j] = permut[j], permut[i-1]
            break
    # 역으로 찾았으니 다시 역으로 바꿔줌
    answer = permut[:i] + sorted(permut[i:], reverse = True)
    print(" ".join(map(str, answer)))   