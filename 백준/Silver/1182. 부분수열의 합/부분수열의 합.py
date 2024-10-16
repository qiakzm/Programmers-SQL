# 부분수열을 확인하는 브루트포스
def search(lev):
	global N, S, arr, cur_sum, ans

	if lev == N:
		if cur_sum == S:
			ans += 1
		return

	# 인덱스가 lev인 원소 선택 O
	cur_sum += arr[lev]
	search(lev + 1)
	cur_sum -= arr[lev]

	# 인덱스가 lev인 원소 선택 X
	search(lev + 1)


N, S = map(int, input().split())
arr = list(map(int, input().split()))
cur_sum = 0
ans = 0

search(0)
if S == 0:
	ans -= 1
	
print(ans)
