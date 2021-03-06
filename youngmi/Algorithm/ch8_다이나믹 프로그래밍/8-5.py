'''
8장 다이나믹 프로그래밍 실전문제2 - 1로 만들기
난이도: 중하, 풀이시간: 20분, 시간제한: 2초, 메모리제한: 128MB

문제설명
정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다.
a X가 5로 나누어떨어지면, 5로 나눈다.
b X가 3으로 나누어떨어지면, 3으로 나눈다.
c X가 2로 나누어떨어지면, 2로 나눈다.
d X에서 1을 뺀다.

X가 주어졌을 때 연산 4개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값ㅇ르 출력하시오.
예를 들어 정수가 26이면 다음과 같이 계산해서 3번의 연산이 최솟값이다.
1. 26 - 1
2. 25/5 = 5
3. 5/5 = 1

입력조건
첫째 줄에 정수 X가 주어진다.(1<=X<=30,000)

출력조건
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

문제 풀이 아이디어
최대 입력조건에 맞는 배열을 생성(0으로 초기화한다.)

'''
x = int(input())

d = [0] * 30001

for i in range(2,x+1):
    d[i] = d[i-1] + 1 #d[2] = d[1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
        print(i, d[i])
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
        print(i, d[i])
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
        print(i, d[i])

print(d[x])