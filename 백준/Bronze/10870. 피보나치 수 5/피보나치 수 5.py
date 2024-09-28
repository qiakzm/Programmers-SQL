# 피보나치
# 1. 일반적인 반복문으로 풀이
N = int(input())

lst = [-1] * (N+2)
lst[0] = 0
lst[1] = 1

for i in range(2, N+1):
	lst[i] = lst[i-2] + lst[i-1]

print(lst[N])