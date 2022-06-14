# TreeDP, DFS
# 다시 풀기

def solution(sales,links):
    N = len(sales)
    sales = [0]+sales
    tree = [[] for _ in range(N+1)]
    for parents,child in links:
        tree[parents].append(child)
    loss_sale = [[0]*2 for _ in range(N+1)]
    # loss_sale[x][0] = x번 노드가 참석하는 경우
    # loss_sale[x][1] = x번 노드가 불참석하는 경우
    def dfs(node):
        nonlocal loss_sale,tree,sales
        if not tree[node]:
            loss_sale[node][0] = sales[node]
            return

        for child_node in tree[node]:
            dfs(child_node)
            loss_sale[node][0] += min(loss_sale[child_node][0],loss_sale[child_node][1])

        
        loss_sale[node][0] += sales[node]
        atamp_loss = float('inf')
        for child_node in tree[node]:
            atamp_loss = min(loss_sale[child_node][0]-loss_sale[child_node][1],atamp_loss)
        loss_sale[node][1] = max(0,atamp_loss) + loss_sale[node][0] - sales[node]
    dfs(1)
    return min(loss_sale[1])