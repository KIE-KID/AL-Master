'''큐 구현'''

'''1. 리스트로 구현'''
list_queue = []

list_queue.append('item1')
list_queue.append('item2')
list_queue.append('item3')
print(list_queue) # ['item1', 'item2', 'item3']

# 맨처음 요소를 재거해야하기 때문에 인덱스가 0인 요소 pop
print("큐에서 제거한 요소:", list_queue.pop(0)) # 큐에서 제거한 요소: item1

print(list_queue) # ['item2', 'item3']


'''2.collections - deque를 이용한 큐 '''
# 문법적으로 비슷하지만 pop() 대신, popleft()를 사용한다는 점이 다르다.
from collections import deque

deque_queue = deque()

deque_queue.append('item1')
deque_queue.append('item2')
deque_queue.append('item3')
print(deque_queue) # deque(['item1', 'item2', 'item3'])

# 첫번째 요소 제거
print("큐에서 제거한 요소:",deque_queue.popleft()) #  큐에서 제거한 요소: item1
print(deque_queue) # deque(['item2', 'item3'])
