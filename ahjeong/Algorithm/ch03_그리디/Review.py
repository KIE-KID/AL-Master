n, k = map(int, input().split(" "))
result = 0
while n != 1:
    if n % k == 0:
        n = n // k
        result += 1
    else :
        minus = n % k
        n = n - minus
        result += minus

print(result)