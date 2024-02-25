def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    rootx = find(parent, x)
    rooty = find(parent, y)
    if rank[rootx] < rank[rooty]:
        parent[rootx] = rooty
    elif rank[rootx] > rank[rooty]:
        parent[rooty] = rootx
    else:
        parent[rooty] = rootx
        rank[rootx] += 1

def solution(n, costs):
    # 간선을 비용에 따라 오름차순으로 정렬
    costs.sort(key=lambda x: x[2])
    
    parent = [i for i in range(n)] # 부모 노드 초기화
    rank = [0] * n # 랭크(트리의 높이) 초기화
    
    result = 0 # 최소 비용
    e = 0 # 현재 선택된 간선의 수
    
    i = 0 # 정렬된 간선 리스트의 인덱스
    while e < n - 1:
        u, v, w = costs[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)
        
        # 사이클이 형성되지 않는 경우 선택
        if x != y:
            e += 1
            result += w
            union(parent, rank, x, y)
    
    return result
