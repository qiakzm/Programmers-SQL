N = int(input())
temp = []
for i in range(N):
    temp.append(int(input()))
    
temp = sorted(temp)
for i in range(N):
    print(temp[i])