#선택 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i
    for j in range(i+1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j # min_idx의 값보다 j의 값이 작으면 j로 업데이트
    array[min_idx], array[i] = array[i], array[min_idx] # 안쪽 for문을 돌고나면 가장 작은 원소를 발견, 범위내에 가장 앞의 원소와 swap해준다
    print(array) # 정렬 과정 출력

print(array) # 최종 정렬 결과 출력

