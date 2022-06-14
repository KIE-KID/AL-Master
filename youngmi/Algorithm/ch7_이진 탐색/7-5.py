'''
7장 이진탐색 실전문제2 - 부품 찾기
난이도: 중하, 풀이시간: 30분, 시간제한: 1초, 메모리제한: 128MB

문제설명
전자매장 부품 N개
부품의 정수 형태 고유 번호
손님이 M개 종류 부품을 대략 구매
가게 안에 부품이 모두 있는지 확인하는 프로그램 작성

입력조건
첫째 줄에 N이 주어진다.(1<=N<=1,000,000), 가게 부품 개수
둘째 줄에 공백으로 구분하여 1이상 1,000,000이하의 N개 정수가 주어짐, 부품 고유번호
셋째 줄에 정수 M이 주어진다.(1<=M<=1,000,000), 손님이 주문한 부품 개수
넷째 줄에 공백으로 구분하여 1이상 1,000,000이하의 M개 정수가 주어짐, 부품 고유번호

출력조건
첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를 없으면 no를 출력한다.

문제풀이 아이디어
이진 탐색 알고리즘
일단 가게 부품 n개를 정렬한다.
for문으로 m개의 부품의 유무를 체크
none이라면 no를 출력
전부 확인했을 때 있으면 yes를 출력
'''
# 이진 탐색 함수를 정의
def binary_search(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2 # 중간점 index 구하기, 몫 구하기(소수점 없이 구하기)
        if array[mid] == target:
            # 찾고자 하는 값이 중간값과 같으면, mid index 구하기
            return mid
        elif array[mid] > target:
            # 중간점이 target 값 보다 크다면 오른쪽만 확인한다
            end = mid - 1
        else:
            start = mid + 1
    # 찾지 못했다면
    return None

N = int(input()) # N, 가게 부품 개수
n_array = list(map(int, input().split())) # 가게 부품 고유 번호 리스트, 공백 구분
M = int(input()) # M, 주문 부품 개수
m_array = list(map(int, input().split())) # 주분 부품 고유 번호 리스트, 공백 구분

n_array.sort() # 탐색 기준 리스트 정렬

# 요청한 부품을 하나씩 확인
for i in m_array:
    result = binary_search(n_array, 0, N - 1, i)
    if result is None:
        print("no", end=' ')
    else:
        print("yes", end=' ')