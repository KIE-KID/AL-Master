N = input()
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x = int(N[-1])
if N[0] in alpha:
    y = alpha.index(N[0]) + 1
dx = [1, -1, 1, -1, 2, 2, -2, -2]
dy = [2, 2, -2, -2, 1, -1, 1, -1]
count = 0

for i in range(8):
    x2 = x + dx[i]
    y2 = y + dy[i]
    if (x2 > 0 and x2 <= 8) and (y2 >0 and y2 <= 8):
        count += 1

print(count)