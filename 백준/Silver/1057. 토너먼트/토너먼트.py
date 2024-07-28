N, k_num, l_num = map(int, input().split())
cnt = 0

while k_num != l_num:
    k_num -= k_num // 2
    l_num -= l_num // 2
    cnt += 1

print(cnt)