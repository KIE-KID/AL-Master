'''

전자레인지
'''

t = int(input())
time = [300, 60, 10]
count = [0,0,0]
j=0

for i in time:
    count[j]=t//i
    t = t % i
    j += 1

if t !=0:
    print(-1)
else:
    print(' '.join(map(str,count)))