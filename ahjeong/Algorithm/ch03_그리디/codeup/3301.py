money = int(input())
coin = [50000, 10000,5000, 1000, 500, 100, 50, 10]
count = 0

for i in coin:
    count += money // i     # python 에서는 몫 만 구하려면 // 를 사용
    print(i, ',', money, ',', count)
    money = money % i 
    print('나머지', money)
print(count)

