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

### List Comprehension

리스트 초기화하는 방법 중 하나로, 대괄호([]) 안에 조건문과 반복문을 넣는 방식으로 초기화할 수 있다.

- 한줄의 소스코드로 리스트를 초기화 하는 방법

```python
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
# [1,3,5,7,9,11,13,15,17,19]

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i*i for i in range(1,10)]
# [1,4,9,16,25,36,49,64,81]
```
<!--# 1 ~ 10을 담는 리스트를 만들어봅시다.
_list = [i for i in range(10)]

# 2, 4, 6, ..., 20을 담는 리스트를 만들어봅시다.
_list = [2 * i for i in range(10)]

# 주어진 리스트를 받아 3의 배수만 담는 리스트를 만들어봅시다.
tmp = [random.randrange(1, 200) for i in range(100)]
_list = [i for i in tmp if i % 3 == 0]

# 값이 두개 들어있는 튜플을 받아 리스트를 생성하되, 튜플 내부의 값을 뒤집어서 저장하세요.
list_of_tupel = [(i, j) for i in range(100), for j in range(100, 0, -1)]
_list = [(j, i) for i, j in list_of_tuple]

# 주어진 리스트를 그대로 담되, 15가 넘어가는 값은 15로 바꿔서 저장합시다.
_list = [i if i <= 15 else 15 for i in tmp]

# 두 개의 리스트를 합치되, 가능한 모든 조합을 저장하는 리스트를 만들어봅시다.
x = [i for i in range(5)]
y = [i for i in range(5)]
_list = [(i, j) for i in x, for j in y]
특히 초보자 분들이 많이 헷갈리시는 것이 if의 쓰임새일거에요. 앞쪽에 붙는 if는 삼항 연산자의 if라고 생각하시면 되고, (즉, 값이 앞 조건을 만족하면 어떤 값, 만족하지 못하면 다른 값) 맨 끝에 붙는 if는 값을 넣을지, 뺄지 결정하는 조건이라고 생각하시면 됩니다.-->

- 좀 더 일반적인 소스코드

```python
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)
# [1,3,5,7,9,11,13,15,17,19]
```

- 2차원 리스트 초기화 하는 방법<br>
특정 크기의 2차원 리스트를 초기화할 때는 반드시 리스트 컴프리헨션을 이용해야한다. 그렇지 않으면 의도하지 않은 결과가 나올 수 있다.
  아래의 예시를 보면 array[1][1]만 바뀐것이 아니라, 3개의 리스트에서 인덱스1에 해당하는 원소들의 값이 모두 5로 바뀌었다. 이는 내부적으로 포함된
  4개의 리스트가 모두 동일한 객체에 대한 3개의 레퍼런스로 인식되기 때문이다.

```python
# NxM 크기의 2차원 리스트 초기화
n = 3
m = 3
array = [[0] * m for _ in range(n)]

# [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

# NxM 크기의 2차원 리스트 초기화 - 잘못된 방법
n = 3
m = 4
array = [[0] * m ] * n
# [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

array[1][1] = 5
# [[0,5,0],[0,5,0],[0,5,0],[0,5,0]]
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

### Unpacking & Packing
```python
a, b = map(int, input().split())
```

- unpacking
```python
_list = [1, 2, 3, 4, 5]
print(*_list) # 1 2 3 4 5
```

- packing
```python
a, b, c = [1, 2, 3]
d = a, b, c
print(d) # (1, 2, 3)
```

Dictionary와 Set은 Hash Table 구조를 띄고 있다.
그래서 삽입, 삭제, 탐색 연산의 시간복잡도가 O(1)이다.

### Set

요소의 중복값이 허용되지 않는다.

```python
i_want_to_erase_duplicate_element = [21, 31, 65, 21, 58, 94, 13, 31, 58]
completed_list = list(set(i_want_to_erase_duplicate_element)) # 21, 31, 65, 58, 94, 13

test_list = ['Test', 'test', 'TEST', 'tteesstt']
converted_list = list(set(map(lambda string: string.lower(), test_list))) # test, tteesstt
```

### Dictionary

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

