# import sys

# # def input():
# #     return sys.stdin.readline().rstrip()

# N = int(input())
# if N < 5:
#     if N % 2 != 0:
#         ans = -1
#     else:
#         ans = N // 2
# else:
#     ct, N = divmod(N, 5)
#     if N == 0:
#         ans = ct
#     else:
#         if N % 2 == 0:
#             ct += N // 2
#             ans = ct
#         else:
#             ct += (N + 5) // 2 - 1
#             ans = ct
# print(ans)

n = int(input())
m = [5, 2]
result = 0

if n < 5:
    if n % 2 != 0:
        result = -1
    else:
        result = n // 2
        
else:
    if n % 5 == 0:
        result += n // 5
    else:
        tmp = n//5
        if (n % 5) % 2 == 0:
            result += ((n % 5) // 2)
            result += tmp
        else:
            tmp -= 1
            result += (((n % 5) + 5) // 2)
            result += tmp
print(result)