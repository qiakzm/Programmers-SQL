S = int(input())
W = int(input())

sleep_time = 0
if S >= 20:
    sleep_time = W+24 - S
else:
    sleep_time = W - S
    
print(sleep_time)