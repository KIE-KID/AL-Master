'''
deque 덱
collections 모듈에서 사용할 수 있다.
https://excelsior-cjh.tistory.com/96
'''
import collections

# 1. append(x)
# 오른쪽(마지막)에 요소를 삽입한다.
deq = collections.deque(['c','d'])
deq.append('e')
print(deq) # deque(['c', 'd', 'e'])

# 2. appendleft(x)
# deque은 양방향에서 데이터를 처리할 수 있는 자료구조이다. append() 메소드와 반대로 왼쪽(처음)에 요소를 삽입한다.
deq.appendleft('b')
print(deq) # deque(['b', 'c', 'd','e])

# 3. extend(iterable)
# 리스트의 extend와 마찬가지로 iterable argument(list, str, tuple...)를 오른쪽(마지막)에 elements를 추가(삽입)한다.
# iterable arguement는 arguements의 각 요소를 하나씩 반환 가능한 object를 의미한다.
deq.extend('fg')
print(deq) # deque(['b', 'c', 'd', 'e', 'f', 'g'])

# 4. extendleft(iterable)
# appendleft()와 마찬가지로 왼쪽(앞쪽)에 iterable arguement를 추가한다.
deq.extendleft('a0')
print(deq) # deque(['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g'])

# 5. pop()
# 오른쪽(마지막)에 있는 요소를 제거하고 반환한다.
pop = deq.pop()
print(pop) # g

# 6. popleft()
# 왼쪽(앞쪽)에 있는 요소를 제거하고 반환한다.
pop_left = deq.popleft()
print(pop_left) # 0

# 7. rotate(n)
# 요소들을 n 만큼 회전해주는 메소드이다. 값이 음수이면 왼쪽, 양수이면 오른쪽으로 회전한다.
deq = collections.deque([1,2,3,4,5])
deq.rotate(2)
print(deq) # deque([4, 5, 1, 2, 3])

deq = collections.deque([1,2,3,4,5])
deq.rotate(-2)
print(deq) # deque([3, 4, 5, 1, 2])