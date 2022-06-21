S = input()
board = S.split('.')
n_board = []
for b in board:
    if b == '':
        n_board.append(b)
        continue
    else: # 문자 일 때
        if len(b) % 2 != 0: #2로 나누어 질 수 없으면 -1
            n_board = -1
            print(n_board)
            break
        else:
            if len(b) == 2:
                b = b.replace('X', 'B')
                n_board.append(b)
            else:
                if len(b) % 4 == 0:
                    b = b.replace('X', 'A')
                    n_board.append(b)
                else:
                    ct, n = divmod(len(b), 4)
                    b = 'AAAA'*ct + 'BB'*(n-1)
                    n_board.append(b)
                    
if type(n_board) == type(board):
    n_board = '.'.join(n_board)
    print(n_board)