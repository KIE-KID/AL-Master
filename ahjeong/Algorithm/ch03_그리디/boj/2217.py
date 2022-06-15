# n = int(input())
# w = []
# for i in range(n):
#     w.append(int(input()))

# w.sort(reverse=True)

# max_w = []
# result = 0
# # 로프 개수 만큼
# for i in range(len(w)):
#     if i == 0:
#         result = w[i]
#         max_w.append(w[i])
#     else:   # 1부터
#         if w[i-1] > w[i]:   # 앞의 원소보다 작기만 하다면,
#             result = w[i] * (i+1)
#             max_w.append(result)
#         else:   # 앞의 원소와 같다면,
#             result = max_w[i-1] + w[i-1]
#             max_w.append(result)

# print(max(max_w))


import sys

n = int(input())
w = []
for i in range(n):
    w.append(int(sys.stdin.readline()))

w.sort(reverse=True)

maxw = 0
for i in range(n):
    tmp = w[i] * (i+1)
    if tmp > maxw : maxw = tmp
    
print(maxw)