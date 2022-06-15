'''스택 구현'''
# https://niceman.tistory.com/20
# https://velog.io/@sohyeon00/Python%EC%9C%BC%EB%A1%9C-stackqueue-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0-%EB%B2%88%EC%97%AD-

'''1. 리스트 자료형으로 구현 ****보통 이걸로 자주 구현**** '''
list_stack = []

# PUSH = 리스트에 .append() 함수로 스택에 요소를 추가하는 동작 - O(1)
list_stack.append('item1')
list_stack.append('item2')
list_stack.append('item3')
print(list_stack) # ['item1', 'item2', 'item3']
print(list_stack[::-1]) # 최상단 원소부터 출력, 먼저 나가고자하는 원소부터 출력

# POP = 리스트에 .pop() 함수로 스택의 요소를 제거하는 동작, 가장 마지막(오른쪽)에 들어간 요소부터 제거됨 - O(1)
list_stack.pop()
print(list_stack) # ['item1', 'item2']

list_stack.pop()
print(list_stack) # ['item1']

list_stack.pop()
print(list_stack) # []

'''2. collections - deque를 이용한 스택'''
# deque 객체를 제외하고는 크게 다른 점은 없지만, 성능이 나음
from collections import deque

deque_stack = deque()

# 요소 삽입
deque_stack.append('item1')
deque_stack.append('item2')
deque_stack.append('item3')
print(deque_stack) # deque(['item1', 'item2', 'item3'])

deque_stack.pop()
print(deque_stack) # deque(['item1', 'item2'])

deque_stack.pop()
print(deque_stack) # deque(['item1'])

deque_stack.pop()
print(deque_stack) # deque([])


