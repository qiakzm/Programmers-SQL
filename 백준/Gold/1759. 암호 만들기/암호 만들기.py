# 라이브러리 활용
from itertools import combinations

vows = ['a', 'e', 'i', 'o', 'u']

def is_possible(word):
	global L, C, arr

	vow = 0
	for w in word:
		vow += (w in vows)
	conv = L - vow

	return (vow >= 1 and conv >= 2)


L, C = map(int, input().split())
arr = input().split()

arr.sort()

for word in combinations(arr, L):
	if is_possible(word):
		print(''.join(word))