import itertools

def solution(orders, course):
    
    answer = []
    menu_count = {}     # 나온 조합 몇개인지 카운트
    i = 0

    for c in course:   # 코스요리 메뉴 조합 수 만큼

        menu_count = {}   
        for order in orders:
            if(c > len(order)):
                continue
            posi_menu = list(map(''.join, itertools.combinations(sorted(order), c)))      # 원하는 코스 조합 수 만큼 orders 의 원소 별 알파벳 조합 생성
            # print("posi_meni", posi_menu)
            # 가능한 메뉴 조합이 몇번 등장하는지 count
            for key in posi_menu:    
                if key not in menu_count:
                    menu_count[key] = 1
                else :
                    menu_count[key] += 1
    
        print('menu_count:', menu_count)
        sorted_dict = sorted(menu_count.items(), key = lambda x: x[1], reverse=True)  # 딕셔너리 item 기준으로 정렬]
        if (len(sorted_dict) > 0):
            print('sorted_dict[0][1]', sorted_dict[0][1])
            if(sorted_dict[0][1] < 2):
                continue
            else:
                max_val = sorted_dict[0][1]
            
            for i in range(len(sorted_dict)):
                if(sorted_dict[i][1] == max_val):
                    answer.append(sorted_dict[i][0])
                else:
                    break
            else:
                continue
    answer.sort()
    print(answer)

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])

