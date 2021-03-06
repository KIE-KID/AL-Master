#예를 들어 리스트의 데이터가 튜플로 구성되어 있을 때, 각 데이터의 두 번째 원소를 기준으로 설정하는 경우
#다음과 같은 형태의 소스코드를 작성할 수 있다. 혹은 람다(Lambda)함수를 사용할 수도 있다.

array = [('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[1]

result = sorted(array, key = setting)
#key에는 하나의 함수가 들어가야하며 이는 정렬의 기준이된다.

print(result) # [('바나나', 2), ('당근', 3), ('사과', 5)]