# 문장열로 입력된 시간을 '초' 단위로 바꿔준다.
def str_to_sec(time):
    h, m, s = time.split(':')
    time = (int(h) * 3600) + (int(m) * 60) + int(s)

    return time

def solution(play_time, adv_time, logs):
    answer = ''
    all_time = []
    play_time, adv_time = str_to_sec(play_time), str_to_sec(adv_time)

    # play_time 에서 1초단위의 배열을 만든다. (인덱스 -> 초)
    for i in range(play_time + 1):
        all_time.append(0)

    # 사용자가 재생한 시간의 start/end 를  초 단위로 바꿔준다.
    for i in logs:
        start, end = i.split('-')
        start = str_to_sec(start)
        end = str_to_sec(end)
        all_time[start] += 1    # start 니까 시청 하는 사람 +1
        all_time[end] += -1     # end 니까 시청 하는 사람 -1

    # 한 구간에서 시청 자 수 업데이트
    for time in range(1, len(all_time)):
        all_time[time] = all_time[time] + all_time[time-1]

    # 전체 구간 시청자 수 업데이트 (앞에서 부터 누적)
    for time in range(1, len(all_time)):
        all_time[time] = all_time[time] + all_time[time-1]

    most_view = 0
    max_time = 0
    for i in range(adv_time-1, play_time):        # adv_time ~ play_time 까지 차례로 검사
        if i >= adv_time:   
            if most_view < all_time[i] - all_time[i - adv_time]:    # 0~adv_time, 1~adv_time+1 .. 까지 
                most_view = all_time[i] - all_time[i - adv_time]    # 시청자 수 구하고 max 찾기
                max_time = i - adv_time + 1                         # 그 max 찾은 인덱스를 반환
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1
    h, m = divmod(max_time, 3600)
    m, s = divmod(m, 60)
    max_time = '{:02d}:{:02d}:{:02d}'.format(h, m, s)

    return max_time