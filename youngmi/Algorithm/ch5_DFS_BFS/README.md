# 그래프 탐색 알고리즘
탐색(Search): 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
대표적인 그래프 탐색 알고리즘으로 DFS와 BFS가 있다.

[스택과 큐 설명](https://github.com/Youngmi-Park/AL-Master/tree/main/youngmi/DataStructure)

[재귀함수 설명]()

## DFS(Depth First Search) 깊이 우선 탐색

그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘으로 정점의 자식들을 먼저 탐색하는 방식이다.<br>
스택 자료구조 혹은 재귀함수를 이용한다.<br>

### 동작 과정

1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 있으면 그 노드를 스택에 넣고 방문 처리한다음 다시 dfs를 시행한다. 
   방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.

### 동작 예시

무방향 그래프(방문 기준: 번호가 낮은 인접 노드부터)<br>
인접노드가 여러개일 수 있기때문에 어떤 노드부터 방문할지 결정하기 위한 기준이 필요하다.
이는 문제 요구사항에따라 달라질 수 있고 어떤 노드부터 방문하는지 상관없는 경우도 있다.

start node: 1<br>
  
[step 1] 시작 노드인 '1'을 스택에 삽입하고 방문 처리<br>
  
[step 2] 스택의 최상단 노드인 '1'의 방문하지 않은 인접 노드에는 '2','3','8'이 있다.
그 중 가장 작은 노드인 '2'를 스택에 넣고 방문 처리한다.
  
[step 3] 스택의 최상단 노드인 '2'의 방문하지 않은 인접 노드에는 '7'이 있다.
'7'을 스택에 넣고 방문 처리한다.

[step 4] 스택의 최상단 노드인 '7'의 방문하지 않은 인접 노드에는 '6','8'이 있다.
그 중 가장 작은 노드인 '6'을 스택에 넣고 방문 처리한다.

[step 5] 스택의 최상단 노드인 '6'의 방문하지 않은 인접 노드는 없다.
따라서 스택에서 6번 노드를 꺼낸다.

[step 6] 스택의 최상단 노드인 '7'의 방문하지 않은 인접 노드에는 '8'이 있다.
'8''을 스택에 넣고 방문 처리한다.

이와 같은 과정을 반복했을 때 전체 노드의 탐색 순서(스택에 들어간 순서)는 다음과 같다.<br>
**탐색순서: 1 → 2 → 7 → 6 → 8 → 3 → 4 → 5**

## BFS(Breadth First Search) 너비 우선 탐색
정점과 같은 레벨에 있는 노드들(형제 노드)을 먼저 탐색하는 방식
가까운 노드부터 우선적으로 탐색하며 큐 자료구조를 이용한다.
**큐 자료구조 이용에 대한 숙지가 필요하다.**

### 동작 과정

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리한다.
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 **방문하지 않은 노드를 모두 큐에 삽입**하고 방문처리한다.
3. 더 이상 2번의 과정을 수행할 수 없을 때 까지 반복한다.

### 동작 예시

무방향 그래프(방문 기준: 번호가 낮은 인접 노드부터)<br>
start node: 1<br>
  
[step 1] 시작 노드인 '1'을 큐에 삽입하고 방문 처리<br>
   
[step 2] 큐에서 노드 '1'을 꺼내 방문하지 않은 인접 노드 '2','3','8'을 큐에 삽입하고 방문처리한다.
  
[step 3] 큐에서 노드 '2'를 꺼내 방문하지 않은 인접 노드 '7'을 큐에 삽입하고 방문 처리한다.

[step 4] 큐에서 노드 '3'을 꺼내 방문하지 않은 인접 노드 '4','5'를 큐에 삽입하고 방문 처리한다.

[step 5] 큐에서 노드 '8'을 꺼내 방문하지 않은 인접 노드가 없으면 무시한다.

이와 같은 과정을 반복했을 때 전체 노드의 탐색 순서(큐에 들어간 순서)는 다음과 같다.<br>
**탐색순서: 1 → 2 → 3 → 8 → 7 → 4 → 5 → 6**

**최단거리 문제에서 활용될 수 있다.**

<hr>

### 예제

### 실전문제

<br>

[백준 그래프 이론 문제집](https://www.acmicpc.net/problemset?sort=ac_desc&algo=7)

[백준 그래프 탐색 문제집](https://www.acmicpc.net/problemset?sort=ac_desc&algo=11)

[백준 너비 우선 탐색 문제집](https://www.acmicpc.net/problemset?sort=ac_desc&algo=126)

[백준 깊이 우선 탐색 문제집](https://www.acmicpc.net/problemset?sort=ac_desc&algo=127)
