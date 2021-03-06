## 이진 탐색

### * 순차 탐색(Sequential Sorting)

시간복잡도: O(N)<br>
- 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
- 데이터 개수가 N개일 때 최대 N번의 비교 연산이 필요하다.
- 보통 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용한다.
- 데이터가 아무리 많아도 항상 원하는 원소(데이터)를 찾을 수 있다는 장점이 있다.
- 리스트에 특정 값의 원소가 있는지 체크할 떄도 순차 탐색으로 원소를 확인한다.
- 리스트 자료형에서 특정한 값을 가지는 원소의 개수를 세는 count() 메서드도 내부에서는 순차탐색이 수행된다.

### 이진 탐색(Binary Search)

- 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘(데이터가 무작위일 때는 사용X)
- 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
- 이미 정렬되어 있다면 빠르게 데이터를 찾을 수 있다.

#### 탐색과정

변수: 데이터를 탐색하고자 하는 범위의 위치를 나타내는 시작점, 끝점, 중간점 3개를 사용한다.

찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 것이 이진 탐색의 과정이다.

[예시]

#### 특징

- 시간복잡도: O(logN)
- 한 번 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어든다.(퀵 정렬과 공통점)

이진 탐색을 구현하는 방법 2가지
- [재귀 함수를 이용한 방법 7-2.py]
- [단순 반복문 이용 7-3.py]

#### 트리 자료 구조
#### 이진 탐색 트리

