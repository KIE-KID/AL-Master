# sort 코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array.sort() # 내부 원소가 바로 정렬, 별도의 리스트를 반환하지 않음
print(array) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(array.sort())) # <class 'NoneType'>