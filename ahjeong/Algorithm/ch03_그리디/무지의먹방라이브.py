import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    # 가장 시간이 적게 걸리는 음식부터 제거한다.
    # 음식시간을 기준으로 최소 힙(우선수위 큐) 구성하고, 우선수위는 (섭취시간, 번호) 쌍으로 삽입한다.
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    # 필요한 변수 : 순차적으로 그 음식을 '다' 먹기 위해 사용한 시간, 이전 음식 소요시간, 남은 음식의 개수
    sum_value = 0
    previous = 0
    length = len(food_times)

    # k와 {sum_value + (가장 시간이 적게 걸리는 음식 소요시간 - 직전 음식 소요시간) * 남은 음식 개수}를 비교
    # q[0][0] : q의 0번째 요소의 0번째 --> 0번째 요소의 섭취시간
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous) * length
        length -= 1
        previous = now

    # k보다 시간이 초과되면, 음식 리스트에서 하나씩 찾기
    result = sorted(q, key = lambda x: x[1])    # 음식의 번호 기준으로 정렬
    answer = result[(k-sum_value) % length][1]
    return answer

food_times = [3, 1, 2]
k = 5
solution(food_times, k)