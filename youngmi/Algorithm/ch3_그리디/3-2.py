'''
3장 그리디 실전문제2 - 큰 수의 법칙
난이도: 하, 풀이시간:30분, 시간제한: 1초, 메모리제한: 128MB, 기출: 2019 국가 교육기관 코딩 테스트

문제설명
다양한 수의 배열에서 주어진 수들을 M번 더해서 가장 큰술를 만드는 법칙이다.
단, 특정 인덱스의 수가 연속해서 k번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.

아이디어
일단 정렬해서 큰거부터 최대로 더함,,?
가장 큰수랑 그 다음으로 큰 수만 저장한다
가장 큰수를 k번, 그 다음 큰수를 1번씩 반복해서 더해서 m번 더하고나면 종료
'''

n, m, k =  map(int, input().split()) # 배열크기 n, 숫자가 더해지는 횟수 m, 연속해서 더해질 수 있는 횟수 k
data = list(map(int,input().split())) # 자연수 n개 - 배열로 저장
result1 = 0

# n=5
# m=8
# k=3
# data=[2,4,5,4,6]

data.sort(reverse=True) # 데이터를 내림차순으로 정렬
first_num = data[0] # 가장 큰 수 저장
second_num = data[1] # 그 다음으로 큰 수 저장

while True:
    for i in range(k): # 가장 큰 수 k번 더하기
        if m == 0: # m이 0이면 탈출
            break
        result1 += first_num # 가장 큰 수 더하기
        m -= 1 # 더할 때마다 -1
    if m == 0:
        break
    result1 += second_num # 그 다음으로 큰수 더하기
    m -= 1 # 더할 때마다 -1

print(result1) # 답안 출력

# but 위의 답안은 M의 크기가 10,000이하이므로 적용가능한 방식이다. M의 크기가 100억 이상이 된다면 시간 초과 판정을 받을 수도 있다.

'''
좀 더 효율적인 방법으로 해결하기
정렬과 가장큰수, 다음으로 큰수를 사용하는 것은 동일하다.
가장큰수 k개 그 다음으로 큰수 1개 (k+1)이 int(m/(k+1)) 쌍 만큼 존재하고
나머지가 있는경우 그 수만큼 가장 큰수를 더해주면된다.
'''

result2 = 0

result2 += (int(m/(k+1)) * k) * first_num
result2 += int(m/(k+1)) * second_num
result2 += (m % (k+1)) * first_num

print(result2)


'''
210724 복습
문제 아이디어
입력받은 데이터를 큰 순서대로 정렬하기
가장 큰 숫자와 그 다음으로 큰 숫자를 변수로 기록
가장 큰 숫자는 k번 그 다음으로 큰 숫자는 1번 이걸 반복해서 m번으로 반들면 된다. ex) (1112)(1112)(11)
'''
n, m, k =  map(int, input().split()) # 배열크기 n, 숫자가 더해지는 횟수 m, 연속해서 더해질 수 있는 횟수 k
data = list(map(int,input().split())) # 자연수 n개 - 배열로 저장

data.sort() # 반환하는 리스트x
first = data[-1]
second = data[-2]

# 가장 큰 수가 더해지는 횟수

count = (m // (k+1)) * k
count += m % (k+1)

result = 0
result += count * first
result += (m-count) * second

print(result)
