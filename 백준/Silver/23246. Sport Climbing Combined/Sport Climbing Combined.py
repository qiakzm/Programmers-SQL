N = int(input())

temp = [tuple(map(int, input().split())) for _ in range(N)]

def comp(x):
	return (x[1] * x[2] * x[3], x[1] + x[2] + x[3], x[0])

result = sorted(temp, key = comp)

for b, p, q, r in result[:3]:
	print(b, end = ' ')