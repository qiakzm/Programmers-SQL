temp = []

for _ in range(7):
    name, cnt = input().split()
    temp.append([name, int(cnt)])

temp.sort(key=lambda x:-x[1])
print(temp[0][0])