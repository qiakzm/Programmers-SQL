# 모음 리스트
vows = ['a', 'e', 'i', 'o', 'u']
choose = []

# 모음의 개수는 1개 이상, 자음의 개수는 2개 이상
def is_possible():
	global L, C, choose, arr

	vow = 0
	for c in choose:
		vow += (c in vows)
	con = L - vow

	return (vow >= 1 and con >= 2)

# 조합 알고리즘
def comb(index, level):
	global L, C, choose, arr

	# Base case
	if level == L:
		if is_possible():
			print(''.join(choose))
		return

	# Recursive case
	for i in range(index, C):
		choose.append(arr[i])
		comb(i + 1, level + 1)
		choose.pop()



L, C = map(int, input().split())
arr = input().split()
# 정렬 필요
arr.sort()

comb(0,0)