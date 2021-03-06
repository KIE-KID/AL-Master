# 다이나믹 프로그래밍
메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법이다.
이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 한다.
다이나믹 프로그래밍의 구현은 일방적으로 두가지 방식(탑다운-하향식과 보텀업-상향식)으로 구성된다. 

다이나믹 프로그래밍은 동적 계획법이라고도 부른다.
* 일반적인 프로그래밍 분야에서의 동적 할당(Dynamic Allocation)은 프로그램이 실행되는 도중에 실행에 필요한 메모리를 할당하는 기법을 의미한다.
* 반면에 다이나믹 프로그래밍에서 다이나믹은 별다른 의미없이 사용된 단어이다. 

**중복되는 연산을 줄이자.**
컴퓨터를 활용해도 해결하기 어려운 문제(기존의 알고리즘으로 해결하기 어려운 문제)
- 최적의 해를 구하기에 시간이 많이 필요한 문제
- 메모리 공간이 매우 많이 필요한 문제

컴퓨터는 연산 속도에 한계가 있고 메모리 공간을 사용할 수 있는 데이터의 개수도 한정적이라는 점이 많은 제약을 발생시킨다.
  이러한 문제를 해결하기 위해서는 연산 속도와 메모리 공간을최대한 활용할 수 있는 효율적인 알고리즘을 작성해야 한다.
  (해결하기 어려운 문제에 대해서 깊게 다루는 분야로는 P-NP 문제를 다루는 계산 복잡도 이론이 있다.) 

어떤 문제는 메모리 공간을 약간 더 사용해 연산 속도를 비약적으로 증가시킬 수 있는 방법이 있는데 대표적인 방법이 바로 다이나믹 프로그래밍(동적 계획법)이다.

#### 다이나믹 프로그래밍의 조건
다이나믹 프로그래밍은 문제가 다음의 조건을 만족할 때 사용할 수 있다.
1. 최적 부분 구조(Optimal Substructure): 큰 문제를 작은 문제로 나눌 수있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있다.
2. 중복되는 부분 문제(Overlapping Subproblem): 동일한 작은 문제를 반복적으로 해결해야 한다.

다이나믹 프로그래밍으로 해결할 수 있는 대표적인 예시로 피보나치 수열이 있다.

#### 피보나치 수열
피보나치 수열은 점화식으로 표현할 수 있다.

피보나치 수열은 다음과 같은 형태의 수열이다.
1, 1, 2, 3, 5, 7, 13, 21, 34, 55, 89, …

피보나치 수열을 점화식으로 표현하면 다음과 같다.
a(n) = a(n-1) + a(n-2), a1 = 1, a2 =  / 1 

*점화식이란 인접한 항들 사이의 관계식을 의미한다.

n번째 피보나치 수 = (n-1)번째 피보나치 수 + (n-2)번째 피보나치 수
단, 1번째 피보나치 수 = 1, 2번째 피보나치 수 = 1

프로그래밍에서는 이러한 수열을 배열이나 리스트로 표현할 수 있다. 8-1.py와 같이 재귀 함수로 구현 가능하다.
그러나 이 경우 f(n)함수에서 n이 커지면 커질수록 반복해서 함수를 호출하기때문에 수행 시간이 기하급수적으로 늘어나는 문제가 발생한다.
이 소스코드의 시간 복잡도는 일반적으로 O(2ⁿ)의 지수 시간이 소요된다.(세타 표기법을 사용하면 θ(1.618···ⁿ)으로 표현할 수 있다.)

예를 들어 f(100)은 약 1,000,000,000,000,000,000,000,000,000,000번의 연산을 해야한다.
이는 현대의 2진수 처리 방식을 가진 컴퓨터 구조에 기반한 시스템에서는 연산을 하면 수백억 년을 넘어간다.


#### 다이나밍 프로그래밍의 2가지 방식
탑다운(메모이제이션) 방식은 하향식이라고도 하며 보텀업 방식은 상향식(반복문 이용)이라고도 한다.
다이나믹 프로그래밍의 전형적인 형태는 보텀업 방식이다.
결과 저장용 리스트는 DP 테이블이라고 부른다.
엄밀히 말하면 메모이제이션은 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념을 의미한다. 따라서 메모이제이션은 다이나믹 프로그래밍에 국한된 개념은 아니다.
한번 계산된 결과를 담아 놓기만 하면 ‘캐시를 사용했다’ ‘메모이제이션 기법을 사용했다’ 고 표현할 수 있다.

정리하자면 큰 문제를 작게 나누고, 같은 문제라면 한 번씩만 풀어 문제를 효율적으로 해결하는 알고리즘 기법이다.

메모이제이션을 이용하는 경우 피보나치 수열 함수의 시간 복잡도는 O(N)이다.

#### Q. 다이나믹 프로그래밍과 분할 정복?
다이나믹 프로그래밍과 분할 정복은 모두 최적 부분 구조를 가질 때 사용할 수 있다.
큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있는 상황

다이나믹 프로그래밍과 분할 정복의 차이점은 부분 문제의 중복이다.
다이나믹 프로그래밍 문제에서는 각 부분 문제들이 서로 영향을 미치며 부분 문제가 중복된다.
분할 정복 문제에서는 동일한 부분 문제가 반복적으로 계산되지 않는다.

