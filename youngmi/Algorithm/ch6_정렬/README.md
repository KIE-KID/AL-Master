# 정렬(Sorting)

데이터를 특정한 기준에 따라 순서대로 나열하는 것<br>
일반적으로 문제 상황에 따라서 적절한 알고리즘이 공식처럼 사용된다.
ex) 데이터의 개수가 적을 때, 데이터 개수가 많더라도 데이터 범위가 한정적일 때, 이미 정렬되어 있는 경우 등...

사람은 직관적으로 데이터를 파악하고 계산할 수 있지만 컴퓨터는 정렬을 어떻게 수행할지 알고리즘을 구체적으로 명시해야한다.

##  1. 선택정렬
처리되지 않은 데이터 중에서 **가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것**을 반복한다.

### 동작 예시

초기 데이터: 7 5 9 0 3 1 6 2 4 8

[step 1] 처리되지 않은 데이터(1~10) 중에서 가장 작은 '0'을 선택해 가장 앞에 있는 '7'과 바꾼다.

'0' 정렬 완료  

[step 2] 정렬된 데이터를 제외하고 처리되지 않은 데이터(2~10) 중에서 가장 작은 '1'을 선택해 가장 앞에 있는 '5'와 바꾼다.

'0', '1' 정렬 완료
 
[step 3] 정렬된 데이터를 제외하고 처리되지 않은 데이터(3~n) 중에서 가장 작은 '2'를 선택해 가장 앞에 있는 '9'와 바꾼다.

'0', '1', '2' 정렬 완료

---------- 중략 ----------

[step 10] 위의 과정을 총 9번 반복하면 마지막 데이터는 가만히 두어도 이미 정렬된 상태이므로, 이 단계에서 정렬이 완료된다.

'0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 정렬 완료

### 시간 복잡도
- 탐색 범위는 반복할 때마다 1씩 줄어든다.
- 데이터를 앞으로 보내는 과정은 N-1번 반복한다.
- 매번 탐색 범위만큼 데이터를 하나씩 확인하고 비교해서 가장 작은 데이터를 찾는다(선형탐색).
- 선택정렬은 이중 반복문으로 구현가능하다. = 직관적으로 이해하면, 소스코드 상에 이중 반복문으로 O(N²)이 되었다고 할 수 있다.

구현방식에 따라 사소한 오차는 있을 수 있지만 위의 방식대로 한다면, 연산 횟수는 다음과 같다.
 N + ( N - 1 ) + ( N - 2 ) + ··· + 2 &nbsp; ≒&nbsp; N × ( N + 1 ) / 2 &nbsp;=&nbsp; ( N² + N ) / 2

<big>***Big-O Notation: O(N²)***</big>

### Q. 선택 정렬은 효율적인가?

정렬할 데이터 개수가 100배 늘어나면 이론적으로 수행 시간은 10,000배 늘어난다.
선택 정렬, 퀵 정렬, 기본 정렬 라이브러리의 수행시간을 비교해보면 다음과 같다.(초 단위, 측정 시간은 컴퓨터마다 다를 수 있음)

<small>* 아래 표는 Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz, 2코어 환경에서 측정</small>
<table class="tg">
<thead>
  <tr style="text-align:center">
    <th class="tg-kr4b">데이터 개수(N)</th>
    <th class="tg-acii">선택 정렬</th>
    <th class="tg-acii">퀵 정렬</th>
    <th class="tg-0pky">기본 정렬 라이브러리</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-acii">N = 100</td>
    <td class="tg-acii" style="text-align:right">0.0123</td>
    <td class="tg-acii" style="text-align:right"> 0.00156</td>
    <td class="tg-0pky" style="text-align:right">0.00000753</td>
  </tr>
  <tr>
    <td class="tg-dude">N = 1,000</td>
    <td class="tg-dude" style="text-align:right">0.354</td>
    <td class="tg-dude" style="text-align:right">0.00343</td>
    <td class="tg-0pky" style="text-align:right">0.0000365</td>
  </tr>
  <tr>
    <td class="tg-acii" >N = 10,000</td>
    <td class="tg-acii" style="text-align:right">15.475</td>
    <td class="tg-acii" style="text-align:right">0.0312</td>
    <td class="tg-0pky" style="text-align:right">0.000248</td>
  </tr>
</tbody>
</table>

선택 정렬을 이용하면 데이터 개수가 10,000개 이상일 때 정렬 속도가 급격히 느려지는 것을 확인할 수 있다.
파이썬에 내장된 기본 정렬 라이브러리는 내부적으로 C언어 기반이면 다양한 최적화 테크닉이 포함되어 더욱 빠르게 동작한다.

선택 정렬은 기본 정렬 라이브러리, 다른 알고리즘과 비교했을 때 매우 비효율적이다.
<u>다만, 특정 리스트에서 가장 작은 데이터를 찾는 일이 코딩 테스트에서 잦기때문에 이러한 형태의 소스코드에 익숙해질 필요가 있다.</u>
선택 정렬 소스코드를 자주 작성해볼 것을 권장!




## 2. 삽입정렬
## 3. 합병정렬
## 4. 퀵정렬
## 5. 계수정렬


<hr>

### 예제

### 실전문제

<br>

[백준 그래프 이론 문제집](https://www.acmicpc.net/problemset?sort=ac_desc&algo=7)

[백준 그래프 탐색 문제집](https://www.acmicpc.net/problemset?sort=ac_desc&algo=11)

[백준 너비 우선 탐색 문제집](https://www.acmicpc.net/problemset?sort=ac_desc&algo=126)

[백준 깊이 우선 탐색 문제집](https://www.acmicpc.net/problemset?sort=ac_desc&algo=127)