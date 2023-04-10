class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


def read_graph(filename):
    with open(filename) as f:
        n = int(f.readline())
        graph = [[] for _ in range(n)]
        for i in range(n):
            row = list(map(int, f.readline().split()))
            for j in range(n):
                if row[j] > 0:
                    graph[i].append(Edge(i, j, row[j]))
        return graph


def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = [s]
    visited[s] = True
    while queue:
        u = queue.pop(0)
        for e in graph[u]:
            if not visited[e.v] and e.w > 0:
                visited[e.v] = True
                parent[e.v] = e
                queue.append(e.v)
    return visited[t]


def ford_fulkerson(graph, s, t):
    max_flow = 0
    parent = [None] * len(graph)
    while bfs(graph, s, t, parent):
        path_flow = float("inf")
        v = t
        while v != s:
            e = parent[v]
            path_flow = min(path_flow, e.w)
            v = e.u
        v = t
        while v != s:
            e = parent[v]
            e.w -= path_flow
            for rev_e in graph[e.v]:
                if rev_e.v == e.u:
                    rev_e.w += path_flow
                    break
            v = e.u
        max_flow += path_flow
    return max_flow


graph = read_graph("data.txt")
s, t = 0, len(graph) - 1
max_flow = ford_fulkerson(graph, s, t)
print("Max flow:", max_flow)