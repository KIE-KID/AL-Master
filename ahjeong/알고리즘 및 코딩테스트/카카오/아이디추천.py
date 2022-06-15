def solution(new_id):

    if (len(new_id) >= 1 and len(new_id) <= 1000) :
        new_id = new_id.lower()     # 1단계

        # 2단계
        new_id = new_id.replace('~', '').replace('!', '').replace('@', '').replace('#', '').replace('$', '').replace('%', '').replace('^', '').replace('&', '').replace('*', '').replace('(', '').replace(')', '').replace('=', '').replace('+', '').replace('[', '').replace('{', '').replace(']', '').replace('}', '').replace(':', '').replace(',', '').replace('<', '').replace('>', '').replace('/', '').replace(']', '').replace('?', '')      

        new_id_list = list(new_id)  # string -> list

        i = 0   # 3단계
        while(i != len(new_id_list) - 1):
            if (new_id_list[i] == '.' and new_id_list[i+1] == '.'):
                del new_id_list[i]
            else :
                i += 1

        new_id = ''.join(new_id_list)   #list -> string

        new_id_list = list(new_id)   # string -> list

        if (new_id_list[0] == '.') :     # 4단계
            del new_id_list[0]

        if (len(new_id_list) != 0 and new_id_list[-1] == '.') :
            del new_id_list[-1]

        new_id = ''.join(new_id_list)

        if(len(new_id_list) == 0):  # 5단계
            new_id_list.append('a')

        if(len(new_id_list) >= 16) :    # 6단계
            new_id = new_id[0:15]  
            new_id_list = list(new_id)
            if (new_id_list[-1] == '.'):
                del(new_id_list[-1])

        new_id = ''.join(new_id_list)   # list -> string

        if (len(new_id_list) <= 2):  # 7단계
            while(len(new_id_list) != 3): 
                new_id_list.append(new_id_list[-1])

        new_id = ''.join(new_id_list)   # list -> string

        return new_id
    else : 
        return 0
