import sys

N = int(sys.stdin.readline())
people = []

for i in range(N):
    inp = sys.stdin.readline()
    people.append(int(inp))


people.sort(reverse=True)
tip = 0
    
for i in range(len(people)):
    tmp = (people[i]+1) - (i+1)
    if tmp > 0:
        tip += tmp
print(tip)