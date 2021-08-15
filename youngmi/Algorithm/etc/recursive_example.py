def recursive_function(n):
    print('재귀함수', n)
    recursive_function(n + 1)


def recursive_function_exit(n):
    if n == 5: # 종료 조건(exit condition)
        print('종료 조건 만족')
        return  # 5번째 호출을 했을 때 종료되도록 종료 조건 명시
    print(n, '번째 재귀함수에서', n + 1, '번째 재귀함수를 호출합니다.')
    recursive_function_exit(n + 1)
    print(n, '번째 재귀함수를 종료합니다.')


# recursive_function(1)
recursive_function_exit(1)
