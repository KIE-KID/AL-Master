
n = 1260
count = 0

#큰 단위 동전부터 확인
coin = [500, 100, 50, 10]

for i in coin:
    count += n // i # 거슬러 줄 수 있는 동전 개수 세기
    n %= i # 해당 동전으로 나눈 나머지

print(count) # 동전 개수

