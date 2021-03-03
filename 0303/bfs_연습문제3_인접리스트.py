# 7 8 (node, edge)
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

def bfs(s, v):
    q = []  # 큐 생성
    visited = [0] * (v + 1)  # visited 생성
    q.append(s)
    visited[s] = 1

    while q:  # 시작지점 다음에 대기중인 번호가 있으면
        p = q.pop(0)  # 맨 앞에 있는 것부터 꺼냄
        print(p)  # do(p)
        # 인접 노드가 방문안한 상태면
        for i in adjlist[p]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

v, e = map(int, input().split())
edge = list(map(int, input().split()))

# 인접리스트
adjlist = [[] for _ in range(v+1)]
for i in range(0, e*2, 2):
    adjlist[edge[i]].append(edge[i+1])
    adjlist[edge[i+1]].append(edge[i])

bfs(1, v)