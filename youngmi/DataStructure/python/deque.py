'''
deque 덱
collections 모듈에서 사용할 수 있다.
https://excelsior-cjh.tistory.com/96
'''
import collections

# 1. append(), list와 마찬가지로 오른쪽(마지막)에 요소를 삽입한다.
deq = collections.deque(['b','c'])
deq.append('d')
print(deq) # deque(['b', 'c', 'd'])

# 2. appendleft(), deque은 양방향에서 데이터를 처리할 수 있는 자료구조이다. append() 메소드와 반대로 왼쪽(처음)에 요소를 삽입한다.
deq.appendleft('a')
print(deq) # deque(['a', 'b', 'c', 'd'])

# 3. extend()

# 4. extendleft()

# 5. pop()

# 6. popleft()

# 7. rotate(n)