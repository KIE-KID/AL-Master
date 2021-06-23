# CHAPTER 3. Greedy 

**그리디 알고리즘**: 탐욕법, 현재 상황에서 가장 좋아 보이는 것만을 선택하는 알고리즘

시간상으로 매우 효율적이지만, 순간마다 최선의 선택을 하는 방법으로 항상 최적화되지 않음으로 최종 답이 최적이 아닐 가능성이 있다.
그 때문에 순간의 최적해가 전체 문제의 최적해가 되어야 사용할 수 있다.
<br>

사전에 외우고 있지 않아도 풀 가능성이 높은 문제 유형이지만, 많은 유형을 접해보고 훈련해야 한다.

창의력, 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력이 필요!

그 대상이 무엇인지 고민해보고 푸는 것이 중요하다.

<small>ex) 가장 큰 순서대로, 가장 작은 순서대로 등...</small>
<br>


# CHAPTER 4. Implementation

보통 사소한 입력 조건 등을 문제에서 명시해주며 문제의 길이가 꽤 긴 편이다. 
그러나, 고차원적인 사고력을 요구하지는 않는 경우가 많아서 문법에 익숙하다면 오히려 쉽게 풀 수 있는 유형
문자열을 처리하거나 큰 정수를 처리하는 문제가 출제되는 경우가 많은데 파이썬은 상대적으로 쉽게 해결할 수 있다.

- 완전 탐색

- 시뮬레이션

코딩 테스트에서는 메모리 사용량 제한보다 더 적은 크기의 메모리를 사용해야 한다. 보통 C/C++보다 파이썬은 동작 속도가 느린데, 내 코드가 1초에 2,000만 번의 연산을 수행한다고 가정하고 문제를 풀면 시간제한에 안정적이다.

***시간제한 1초, 데이터 개수 100만 개인 문제는 일반적으로 시간 복잡도 O(NlogN) 이내의 알고리즘으로 풀어야 한다.***

**예를 들어 N = 1,000,000일 때 NlogN = 약 20,000,000이다. 알고리즘 문제를 풀 때는 시간제한과 데이터 개수를 먼저 확인하고 어느 정도의 시간 복잡도의 알고리즘으로 작성해야 풀 수 있을 것인지 예측할 수 있어야 한다.**

카카오 공채에서 API 개발 문제가 출제된 적 있다. 카카오 문제 풀이 서버와 통신하는 프로그램 모듈을 작성해야 했는데, 이는 웹 서버와 데이터 분석에 대한 기초 지식도 필요한 부분이다.!
<br>

# CHAPTER 5. DFS, BFS

#### 1. DFS(Depth First Search) 깊이 우선 탐색
정점의 자식들을 먼저 탐색하는 방식

#### 2. BFS(Breadth First Search) 너비 우선 탐색
정점과 같은 레벨에 있는 노드들(형제 노드)을 먼저 탐색하는 방식
<br>

# CHAPTER 6. 정렬

데이터를 특정한 기준에 따라 순서대로 나열하는 것<br>
일반적으로 문제 상황에 따라서 적절한 알고리즘이 공식처럼 사용된다.

1. 선택정렬
2. 삽입정렬
3. 합병정렬
4. 퀵정렬
5. 계수정렬

<table style="text-align:center" class="tg">
<thead>
  <tr>
    <th class="tg-kr4b"></th>
    <th class="tg-acii">Best</th>
    <th class="tg-acii">Avg</th>
    <th class="tg-acii">Worst</th>
    <th class="tg-acii">Stable</th>
    <th class="tg-0pky">In-Place</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-acii">삽입 정렬(Insertion Sort)</td>
    <td class="tg-acii">N</td>
    <td class="tg-acii">N²</td>
    <td class="tg-acii">N²</td>
    <td class="tg-acii">O</td>
    <td class="tg-0pky">O</td>
  </tr>
  <tr>
    <td class="tg-dude">퀵 정렬(Quick Sort)</td>
    <td class="tg-dude">NlogN</td>
    <td class="tg-dude">NlogN</td>
    <td class="tg-dude">N²</td>
    <td class="tg-dude">X</td>
    <td class="tg-0pky">O</td>
  </tr>
  <tr>
    <td class="tg-acii">합병 정렬(Merge Sort)</td>
    <td class="tg-acii">NlogN</td>
    <td class="tg-acii">NlogN</td>
    <td class="tg-acii">NlogN</td>
    <td class="tg-acii">O</td>
    <td class="tg-0pky">X</td>
  </tr>
  <tr>
    <td class="tg-dude">힙 정렬(Heap Sort)</td>
    <td class="tg-dude">NlogN</td>
    <td class="tg-dude">NlogN</td>
    <td class="tg-dude">NlogN</td>
    <td class="tg-dude">X</td>
    <td class="tg-0pky">O</td>
  </tr>
  <tr>
    <td class="tg-acii">계수정렬(Counting Sort)</td>
    <td class="tg-acii">N</td>
    <td class="tg-acii">N</td>
    <td class="tg-acii">N</td>
    <td class="tg-acii">O</td>
    <td class="tg-0pky">X</td>
  </tr>
  <tr>
    <td class="tg-dude">기수 정렬 (Radix Sort)</td>
    <td class="tg-dude">N</td>
    <td class="tg-0pky">N</td>
    <td class="tg-0pky">N</td>
    <td class="tg-0pky">O</td>
    <td class="tg-0pky">X</td>
  </tr>
</tbody>
</table>

|                           | Best  |  Avg  | Worst | Stable | In-Place |
| ------------------------- | :---: | :---: | :---: | :----: | :------: |
| 삽입 정렬(Insertion Sort) |   N   |  N²   |  N²   |   O    |    O     |
| 퀵 정렬(Quick Sort)       | NlogN | NlogN |  N²   |   X    |    O     |
| 합병 정렬(Merge Sort)     | NlogN | NlogN | NlogN |   O    |    X     |
| 힙 정렬(Heap Sort)        | NlogN | NlogN | NlogN |   X    |    O     |
| 계수정렬(Counting Sort)   |   N   |   N   |   N   |   O    |    X     |
| 기수 정렬 (Radix Sort)    |   N   |   N   |   N   |   O    |    X     |

