# 힙 라이브러리 사용 예제2, 최대 힙 O(NlogN)
import heapq


# 내림차순 힙 정렬(Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)  # 마이너스로 넣으면 역순으로 삽입됨.

    # 힙에 삽입된 모든 원소를 차례때로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))  # 마이너스 부호를 붙여서 꺼낸다.
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
