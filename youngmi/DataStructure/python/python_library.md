표준 라이브러리<br>
특정한 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리를 의미한다

1.itertools<br>
효율적인 반복을 위한 함수, 반복되는 형태의 데이터를 처리하는 기능을 제공하고 순열과 조합 라이브러리를 제공한다.
- permutations
- combinations
- products

2. re <br>
정규식 연산, 텍스트 처리 서비스

3. collections <br>
   컨테이너 데이터형
- deque
- counter

4. heapq<br> 
   힙 큐 알고리즘, heap을 활용한 priority queue 구현할 때 사용

- heapq 
    - heapq.heappush() : 원소 삽입
    - heapq.heappop() : 원소 꺼내기

5. bisect 
배열 이진 분할 알고리즘
- 이진 탐색(binary search)
    - bisect_left
    - bisect_right
    
6. math
수학적 기능을 제공하는 라이브러리
- math.factorial()
- math.sqrt()
- math.gcd()
- math.pi
- math.e
    

내장함수
기본 입출력 기능부터 정렬 기능을 포함하고 있는 기본 내장 라이브러리
종류

- input()
- print()
- sum(iterable)
- min(), max()
- eval()
- sorted(iterable,key = , reverse = bool)
- iterable.sort(key = , reverse = bool)



https://velog.io/@koyo/python-docs-6