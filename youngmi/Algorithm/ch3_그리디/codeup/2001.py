'''
2001 : 최소 대금
시간 제한: 1 Sec  메모리 제한: 128 MB
제출: 6346  해결 문제 수: 3350  성공률: 52.8%
link: https://www.codeup.kr/problem.php?id=2001

풀이한 날짜: 2021년 4월 18일

문제설명
파파 파스타 가게는 점심 추천 파스타와 생과일 쥬스 세트 메뉴가 인기가 좋다.
이 세트 메뉴를 주문하면 그 날의 3 종류의 파스타와 2 종류의 생과일 쥬스에서 하나씩 선택한다.
파스타와 생과일 쥬스의 가격 합계에서 10%를 더한 금액이 대금된다.
어느 날의 파스타와 생과일 쥬스의 가격이 주어 졌을 때, 그 날 세트 메뉴의 대금의 최소값을 구하는 프로그램을 작성하라.
'''

min_p = 3000
min_j = 3000
result = 0

for i in range(3):
    temp = int(input())
    min_p = min(min_p, temp)
for j in range(2):
    temp = int(input())
    min_j = min(min_j, temp)

result = (min_j+min_p) * 1.1
print(round(result,1))