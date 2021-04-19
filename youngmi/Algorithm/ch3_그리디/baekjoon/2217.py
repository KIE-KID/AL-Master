'''
2217
로프

'''
import sys
input = sys.stdin.readline # 즐 개수
n = int(input())
w = [int(input()) for _ in range(n)]

max_w = 0
w.sort(reverse=True)
for j in range(n):
    temp = w[j] * (j+1)  # 들 수 있는 최대 중량
    max_w = max(temp, max_w)

print(max_w)