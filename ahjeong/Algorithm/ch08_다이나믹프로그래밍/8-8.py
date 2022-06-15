# n, m = map(int, input().split())
#
# array = []
# for i in range(n):
#     array.append(int(input()))
#
# # 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
# d = [10001]*(m+1)
#
# # 다이나믹 프로그래밍 진행(보텀업)
# d[0] = 0
# for i in range(n):
#     for j in range(array[i], m+1):
#         if d[j-array[i]] != 10001:      # (i-k) 원을 만드는 방법이 존재하는 경우
#             d[j] = min(d[j], d[j-array[i]] + 1)
#
# # 계산된 결과 출력
# if d[m] == 10001:   # 최종적으로 M원을 만드는 방법이 없을 경우
#     print(-1)
# else:
#     print(d[m])

# 아정 풀이
# 문제점 : 예제 케이스만 동작, 아이디어는 비슷하지만 min 값을 비교하는 부분을 조정할 필요가 있다.
# n, m = map(int, input().split())
# won = []
# for i in range(n):
#     won.append(int(input()))
#
# d = [0]*10000
# for i in won:
#     d[i] = 1
#
# for i in range(n+2, m+1):
#     d[i] = min(d[2] + d[i-2], d[3] + d[i-3])
#     print(d[0:m+1])
#
# if d[m] == 0:
#     print("-1")
# else:
#     print(d[m])
