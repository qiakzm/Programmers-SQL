def permut(level):
	global N, choose, check

	# Base case
	if level == N:
		print(' '.join(map(str, choose)))
		return

	# Recursive case
	for i in range(1, N + 1):
		if check[i] == True:
			continue

		choose.append(i)
		check[i] = True

		permut(level + 1)

		check[i] = False
		choose.pop()


N = int(input())
choose = []
check = [False] * (N + 1)
permut(0)
