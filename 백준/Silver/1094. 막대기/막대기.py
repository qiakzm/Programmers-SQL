X = int(input())
ran = [64, 32, 16, 8, 4, 2, 1]
cnt = 0

for i in ran:
    while X - i >= 0:
        X -= i
        cnt += 1
        
print(cnt)