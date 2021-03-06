'''
3301 : 거스름돈
시간 제한: 1 Sec  메모리 제한: 128 MB
제출: 5028  해결 문제 수: 2941  성공률: 58.5%
link: https://www.codeup.kr/problem.php?id=3301

풀이한 날짜: 2021년 4월 18일
풀이시간: 10분 내외

문제설명
어떤 가게의 욕심쟁이 점원은 거스름돈을 나눠줄때 거스름돈의 개수를 적게해서 주고자 한다.
거스름돈을 입력 받아 점원이 줄 수 있는 최소 거스름돈의 개수를 출력하시오.
예를 들어 54520원인 경우,
거스름돈으로 50000원권 1장, 1000원권 4장, 500원 1개, 10원 2개 해서 총 8개이다.
(※ 현재 우리나라가 사용하고 있는 화폐를 사용한다. 10원 50원 100원 500원 1,000원 5,000원 10,000원 50,000원)

입력
거스름돈 n이 입력된다. ( n은10이상의  int 범위 )

출력
최소 거스름돈의 개수를 출력한다.
'''

# 책의 예제 3-1 거스름돈 문제와 유사

n = int(input()) # 입력받은 거스름 돈
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10] # 화폐 단위
count = 0 # 거스름 돈 개수

for i in money:
     count += n//i # 거슬러 줄 수 있는 동전 개수 세기
     n %= i # 해당 동전으로 나눈 나머지

print(count)