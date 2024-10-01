from itertools import permutations

N = int(input())

for permut in permutations(range(1, N + 1)):
	print(' '.join(map(str, permut)))