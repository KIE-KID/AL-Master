money = int(input())
coin = [50000, 10000,5000, 1000, 500, 50, 10]
count = 0

for i in coin:
    count += money // i
    money = money % i
    print(money, count)
print(count)