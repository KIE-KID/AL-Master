# 난이도 (하)
# 풀이 시간 : 5분
# 아이디어 : 가장 큰 수와 두번째로 큰 수가 필요하다. 반복되는 수열을 파악한다.
# 1. 단순하게 푸는 방법

# N, M, K  를 공백으로 구분
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
# 제일 큰 수 2개
first = data[-1]
second = data[-2]

# 계산
result = 0
while(True):
    for i in range(k):
        if m == 0:
            break;
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
print(result)

    
# 2.간단한 수학적 아이디어를 이용한 방법
# 계산 부분만 다름
 
# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first   # 가장 큰 수 더하기
result += (m-count) * second    # 두번째로 큰 수 더하기

# 아정 풀이
# 문제점 : m 이 (k+1) 로 나누어 떨어지는 경우만 고려함
data.sort()

max1 = data[-1]
max2 = data[-2]

result = max1 * k * (m // k) + max2 * (m % k)
