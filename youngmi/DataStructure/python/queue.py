'''큐 구현'''

'''1. 리스트 자료형으로 구현 '''
list_queue = []

list_queue.append('item1')
list_queue.append('item2')
list_queue.append('item3')
print(list_queue) # ['item1', 'item2', 'item3']

# 맨처음 요소를 재거해야하기 때문에 인덱스가 0인 요소 pop
print("큐에서 제거한 요소:", list_queue.pop(0)) # 큐에서 제거한 요소: item1

print(list_queue) # ['item2', 'item3']


'''2.collections - deque를 이용한 큐 ****보통 이걸로 자주 구현**** '''
# 문법적으로 비슷하지만 pop() 대신, popleft()를 사용한다는 점이 다르다.
# 리스트자료형으로도 구현할 수는 있지만 시간복잡도가 높아서 비효율적으로 동작할 수 있기때문에 deque라이브러리를 권장
from collections import deque

deque_queue = deque()

deque_queue.append('item1') # O(1)
deque_queue.append('item2')
deque_queue.append('item3')
print(deque_queue) # deque(['item1', 'item2', 'item3'])

# 첫번째 요소 제거
print("큐에서 제거한 요소:",deque_queue.popleft()) #  큐에서 제거한 요소: item1 - O(1)
print(deque_queue) # deque(['item2', 'item3'])