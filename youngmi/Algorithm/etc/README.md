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
<img style="display:inline" width="350px" src="https://user-images.githubusercontent.com/53163222/128749569-f288fb2e-a80b-4b8c-b566-b6880022380a.png">
</p>