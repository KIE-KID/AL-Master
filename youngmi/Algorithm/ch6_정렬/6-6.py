# 계수 정렬 소스코드
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

#모든 범위를 포함하는 리스트 선언
count = [0] * (max(array) + 1) # 가장 큰수(k)+1 만큼, 모든 항목은 0으로 초기화

# 숫자 개수 세는 것
for i in array: # array를 처음부터 끝까지 돈다.
    count[i] += 1 # 각 데이터에 해당하는 count 리스트의 index의 값을 +1을 해준다.

# 정렬된 결과 출력
for i in range(len(count)):
    print((str(i)+' ') * count[i], end='')

# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i, end=' ')
