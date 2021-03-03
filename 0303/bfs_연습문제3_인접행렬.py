# 7 8 (node, edge)
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

def bfs(s, v):
    q = []                  # 큐 생성
    visited = [0] * (v+1)   # visited 생성
    q.append(s)
    visited[s] = 1

    while q:                # 시작지점 다음에 대기중인 번호가 있으면
        p = q.pop(0)        # 맨 앞에 있는 것부터 꺼냄
        print(p)            # do(p)
        # 인접 노드 중 표시안된 노드가 있고, 방문안한 상태면
        for i in range(1, v+1):
            if adj[p][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = 1
                # visited[i] = visited[p] + 1 이라고 하면 거리가 됨.
                    # 빠진 노드는 visited가 0인 것
                    # visited - 1 는 시작지점으로부터의 최단 거리 (edge의 개수)



v, e = map(int, input().split())
edge = list(map(int, input().split()))

# 인접행렬
adj = [[0] * (v+1) for _ in range(v+1)]
# 무향그래프 생성
for i in range(0, e*2, 2):
    adj[edge[i]][edge[i+1]] = 1
    adj[edge[i+1]][edge[i]] = 1

# for i in range(e):
#     adj[edge[i*2]][edge[i*2+1]] = 1
#     adj[edge[i*2+1]][edge[i*2 ]] = 1

bfs(1, v)
