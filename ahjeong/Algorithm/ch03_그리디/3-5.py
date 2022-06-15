# 난이도 (하)
# 풀이 시간 : 5분
# 아이디어 : 최대한 많이 나누기

# 1. 단순하게 푸는 방법
n, k = map(int, input().split())
result = 0

# N 이 K 이상이라면 K 로 나누기
while n >= k:
    # N 이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1
# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)