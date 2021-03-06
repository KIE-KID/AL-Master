<!--파이썬 문법-->
<!--알아야 하는 문법, 자주 쓰이는 것, 헷갈리는 것, 기타 등등 기록용-->

## 코딩 테스트를 위한 파이썬 문법

### 수 자료형 

```python
a / b # 나누기
a % b # 나머지
a // b # 몫
a ** b # 거듭제곱

round(num, 반올림 할 자리) # 반올림
```

### 리스트 자료형

여러 개의 데이터를 연속적으로 담아 처리하기 위해 사용할 수 있으며, C나 자바와 같은 언어의 배열(array) 기능을 포함한다.내부적으로는 연결 리스트 자료구조를 채택하고 있으며 C++의 STL vector와 유사하다. 리스트 대신 배열 혹은 테이블 이라고 부르기도 한다.

```python
a = list() # 빈 리스트 선언1
a = [] # 빈 리스트 선언2

a = [0] * 10 # 모든 값이 0이고 크기가 10인 1차원 리스트 초기화
```

### 리스트 메서드

|  함수명   | 사용법                                       | 설명                                                         | 시간 복잡도 |
| :-------: | -------------------------------------------- | ------------------------------------------------------------ | :---------: |
| append()  | 변수명.append()                              | 원소를 하나 삽입할 때                                        |   *O(1)*    |
|  sort()   | 변수명.sort()<br />변수명.sort(reverse=True) | 기본 정렬 기능, 오름차순 정렬<br />내림차순 정렬             | *O(NlogN)*  |
| reverse() | 변수명.revers()                              | 원소의 순서를 모두 뒤집어 놓는다.                            |   *O(N)*    |
| insert()  | 변수명.insert(삽입할 위치 인덱스, 삽입할 값) | 특정 인덱스 위치에 원소를 삽입할 때                          |   *O(N)*    |
|  count()  | 변수명.count(특정값)                         | 리스트에서 특정한 값을 가지는 데이터의 개수를 셀 때          |   *O(N)*    |
| remove()  | 변수명.remove(특정값)                        | 특정한 값을 갖는 원소를 제거하는데, 값을 가진 원소가 여러 개면 하나만 제거한다. |   *O(N)*    |


*insert(), append(), remove() 눈여겨 보기*
코테에서 insert()를 사용할 때 원소의 개수가 N개면, 시간복잡도는 O(N)이다. append()는 O(1)에 수행되는 반면, insert()는 
느리다는 것을 알 수 있다.(중간에 원소를 삽입한 뒤에, 리스트의 원소 위치를 조정해줘야하기 때문이다.)
따라서 insert()를 너무 많이쓰면 '시간초과'로 테스트를 통과하지 못할 수됴 있다.
remove()의 시간 복잡도도 insert()와 마찬가지로 O(N)이다.(리스트 중간에 있는 원소를 삭제한 뒤에, 리스트의 원소 위치를 조정해주어야 하기 때문에)

Q. 특정한 값의 원소를 모두 제거하려면?<br>
파이썬에서는 remove_all()과 같은 특정값을 가지는 모든 원소를 제거하는 함수가 없으므로 아래의 방법을 이용한다.

```python
# a의 원소를 하나씩 확인하며 remove_set에 포함되어 있지 않을때만 리스트 변수인 result에 넣는다.
a = [1,2,3,4,5,5,5]
remove_set = {3,5}

result = [i for i in a if i not in remove_set]
#result = [1,2,4]
```

int형 리스트 join
```python
' '.join(map(str,변수명))
```

### Packing & Unpacking
```python
a, b = map(int, input().split())
```

#### packing

- 하나의 변수에 여러개의 값을 넣는 것

```python
a, b, c = [1, 2, 3]
d = a, b, c
print(d) # (1, 2, 3)
```

#### unpacking

- 패킹되어있는 변수에서 여러 값을 꺼내오는 것

```python
_list = [1, 2, 3, 4, 5]
print(*_list) # 1 2 3 4 5
```


### Set & Dictionary
Set과 Dictionary는 Hash Table 구조를 띄고 있다.
그래서 삽입, 삭제, 탐색 연산의 시간복잡도가 O(1)이다.

#### Set

요소의 중복값이 허용되지 않는다.

```python
i_want_to_erase_duplicate_element = [21, 31, 65, 21, 58, 94, 13, 31, 58]
completed_list = list(set(i_want_to_erase_duplicate_element)) # 21, 31, 65, 58, 94, 13

test_list = ['Test', 'test', 'TEST', 'tteesstt']
converted_list = list(set(map(lambda string: string.lower(), test_list))) # test, tteesstt
```

#### Dictionary

딕셔너리는 키와 값이 쌍을 이루고 있다.
dictionary를 생성할때는 **zip**을 사용할 수 있다.

> 각 iterables의 요소들을 모으는 이터레이터를 만든다.
```python
fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]

_dict = dict(zip(fruit, price)) # {'apple' : 3200, 'grape' : 15200, 'orange' : 9000, 'banana' : 5000}
```

딕셔너리에서 값을 찾을 때, 없는 값을 찾는 경우
if나 in을 사용하지 않고 출력하는 방법
```python
print(_dict['strawberry']) # Error!
print(_dict.setdefault('strawberry', 0)) # 0
```
setdefault는 딕셔너리에 값이 있을 땐 해당 값을 리턴하고, 값이 없을 땐 두번째 인자로 넘겨준 값을 추가하고 추가한 값을 리턴한다.

dictionary의 원소를 unpacking 할 때
```python
print(*_dict.keys()) # apple grape orange banana
print(*_dict.values()) # 3200 15200 9800 5000
print(*_dict.items()) # ('apple', 3200) ('grape', 15200) ('orange', 9800) ('banana', 5000)
```

### Sorting

`sort()`: 리스트를 내부 정렬하는 메소드
`sorted()`:  컨테이너형 데이터를 받아 정렬된 리스트를 돌려주는 함수
```python
_list = [5, 6, 4, 8, 2, 3]
sorted_list = sorted(_list) #    2, 3, 4, 5, 6, 8
_list.sort()
print(_list) # 2, 3, 4, 5, 6, 8

_set = {65, 12, 15, 156, 31, 54, 94, 82, 31}
_set.sort() # Error!!!!
print(sorted(_set)) # 12, 15, 31, 54, 65, 82, 94, 156
```

내림차순 정렬
```python
_list = [5, 6, 4, 8, 2, 3]
sorted_list = sorted(_list, reversed = True) # 8, 6, 5, 4, 3, 2
```

튜플의 첫번째 값을 기준으로 정렬
```python
_list = [(1, 3), (8, 2), (2, 5), (4, 7)]
sorted_list = sorted(_list, key = lambda dt: dt[1]) # (8, 2), (1, 3), (2, 5), (4, 7)
```
key는 함수를 입력 받는다. 즉, lambda가 함수라는 것을 알 수 있다.
정확히 말해서, lambda는 익명 함수라는 것으로, 함수의 이름을 명시하지 않고 일회성으로 사용하기 위해 정의하는 것이다. 여기서 dt는 함수에서 사용할 변수명으로, dt는 각각의 튜플을 저런식으로 사용하겠다는 것이다.

튜플의 리스트를 첫번째 값으로 오름차순 정렬을 하는데 값이 같으면 두번째 값으로 내림차순 정렬하고 싶을 때
```python
_list = [(1, 3), (8, 2), (2, 5), (4, 7)]
sorted_list = sorted(_list, key = lambda dt: (dt[1], -dt[0])) # (8, 2), (1, 3), (2, 5), (4, 7)
```
조건이 여러개인 경우 다음과 같이 튜플 형태로 묶어주는데, 음수가 되면 내림차순으로 정렬한다고 생각하면 됩니다. (사실은 각각의 값이 음수가 되면 대소관계가 반전되기 때문에, 음수로 변환해서 대소관계를 비교해서 정렬하는 것이다.)

lambda를 사용하면 정말 다양한 방식으로 정렬을 할 수 있다.
```python
_list = ["CHicken", "hamburger", "Sushi", "chocolate"]

print(sorted(_list)) # ['CHicken', 'Sushi', 'chocolate', 'hamburger']
print(sorted(_list, key = lambda dt: dt.lower())) # ['CHicken', 'chocolate', 'hamburger', 'Sushi']
```
일반적으로 문자열은 대소관계를 비교하기 때문에, 다음과 같이 모두 소문자로 바꿔버리면 대소관계 상관 없이 정렬을 할 수 있다.
``
