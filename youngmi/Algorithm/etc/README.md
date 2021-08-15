# 재귀 함수

재귀 함수(Recursive Function)란 자기 자신을 다시 호출하는 함수를 의미한다.

문자열을 무한히 출력하는 예제
``` python
def recursive_function(n):
    print('재귀함수', n)
    recursive_function(n+1)

recursive_function(1)
```

파이썬에서는 최대 재귀 깊이 제한이 있기때문에 위의 코드를 실행하면 어느 정도 출력하다 오류 메시지가 출력되고 프로그램이 종료될 수 있다.

<p>
<img style="display:inline" width="80px" src="https://user-images.githubusercontent.com/53163222/128749035-d1343a1b-47ac-4d7a-81a7-978b208be346.png">
<img style="display:inline" width="370px" src="https://user-images.githubusercontent.com/53163222/128750452-d453ad64-12d2-469c-afec-c023630012dc.png">
</p>

함수가 재귀적으로 호출되게 되면 컴퓨터 시스템의 스택에 함수가 반복적으로 쌓여서 제일 위에 쌓인 것부터 처리된다.
컴퓨터 메모리는 한정된 자원(크기)이기 때문에 무한 호출하는 재귀 함수는 빠르게 메모리가 차서 문제가 발생한다. 그래서 재귀 깊이 제한이 있다.

만약 제한없이 재귀 함수를 호출하고 싶다면 재귀 제한을 느슨하게 만들어주거나 별도의 스택 자료구조를 이용해서 스택객체를 따로 만드는 방법을 이용할 수도 있다.

일반적인 코딩테스트에서 재귀 함수를 문제 풀이에 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야한다.
종료조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있다.

종료 조건을 명시한 재귀 함수x`
``` python
def recursive_function_exit(n):
    if n == 5: # 종료 조건(exit condition)
        print('종료 조건 만족')
        return  # 5번째 호출을 했을 때 종료되도록 종료 조건 명시
    print(n, '번째 재귀함수에서', n + 1, '번째 재귀함수를 호출합니다.')
    recursive_function_exit(n + 1)
    print(n, '번째 재귀함수를 종료합니다.')
``` 

<p align="center">
<img width="40%" src="https://user-images.githubusercontent.com/53163222/128752174-cf3b2a41-f2c0-4df1-bdc1-ed3089b016b1.png">
</p>

재귀 함수로 코드를 작성하면 점화식을 그대로 이용하기 때문에 반복문으로 작성할 때보다 코드가 더 간결하고 직관적으로 작성할 수 있다.
그러나 다른 사람이 이해하기 어려운 형태의 코드가 될 수도 있으므로 신중하게 사용해야 한다.
- 모든 재귀 함수는 반복문으로 치환할 수 있다.
- 재귀 함수가 반복문보다 유리한 경우도 있고 불리한 경우도 있다.
- 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓인다.
- 스택을 사용해야할 때 구현상 스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많다.

