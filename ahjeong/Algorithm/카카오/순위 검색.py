from itertools import combinations

import re

def solution(info, query):
    answer = []
    info_list = []
    query_list = []

    # info 전처리
    for i in range(len(info)):
        info_list.append(info[i].split(' '))
    # query 전처리
    for i in range(len(query)):
        q = re.compile('( and)').sub('', query[i]).split()   # query 에서 'and' 와 '-' 를 다 제외
        query_list.append(q)        # 조건만 들어가 있는 리스트

    # 지원자 한명마다 나올 수 있는 조합 찾기
    info_value = {}
    info_combi = []

    for i in range(len(info_list)):
        info_combi = []
        for k in range(5):
        # [0,1,2,3] 4개의 원소로 만들 수 있는 조합 중에서
            for condition in combinations([0,1,2,3], k):
                case = []
                for idx in range(4):
                    if idx not in condition:
                        case.append(info_list[i][idx])
                    else:
                        case.append('-')
                info_combi.append(''.join(case))

        for case in info_combi:
            if case not in info_value.keys():
                info_value[case] = [int(info_list[i][4])]   # value 에 점수
            else:
                info_value[case].append(int(info_list[i][4]))
            case = []

    # 각 조합마다 있는 점수들 오름차순으로 정렬
    for key in info_value.keys():
        info_value[key].sort()

    # 쿼리를 만족하는 지원자 몇명인지 세기
    # query_list : 쿼리 담겨있는 리스트
    for query in query_list:
        q_cnd = ''.join(query[:-1])    # 쿼리 조건
        q_score = int(query[-1])    # 쿼리 점수
        # info_value 딕셔너리에 쿼리가 존재하는지 확인
        if q_cnd in info_value:
            data = info_value[q_cnd]
            if len(data) > 0:
                start, end = 0, len(data)
                while start != end and start != len(data):
                    if data[(start + end) // 2] >= q_score:
                        end = (start + end) // 2
                    else:
                        start = (start + end) // 2 + 1
                # 찾은 인덱스 부터 끝까지 다 만족
                answer.append(len(data) - start)
        else:
            answer.append(0)


    return answer