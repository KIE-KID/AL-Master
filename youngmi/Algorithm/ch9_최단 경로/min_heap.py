# 힙 라이브러리 사용 예제1, 최소 힙 O(NlogN)
import heapq

# 기본적으로 최소 힙 방식으로 라이브러리가 구현되어있음. 우선순위가 낮은 원소부터 나옴.
# 표준 라이브러리의 병합정렬, 퀵 정렬 기반 정렬 알고리즘과 동일한 시간 복잡도
# 오름차순 힙 정렬(Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입 O(logN)
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]