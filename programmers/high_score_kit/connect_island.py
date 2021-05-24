def solution(n, costs):
    answer = 0

    # 비용순으로 정렬
    costs.sort(key=lambda x: x[2])
    # 첫번째부터 시작
    edges = set([costs[0][0]])
    while len(edges) != n:
        for i, cost in enumerate(costs):
            # 사이클 발생하면 포함x
            if cost[0] in edges and cost[1] in edges:
                continue
            if cost[0] in edges or cost[1] in edges:
                edges.update([cost[0], cost[1]])
                answer += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return answer


solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])
