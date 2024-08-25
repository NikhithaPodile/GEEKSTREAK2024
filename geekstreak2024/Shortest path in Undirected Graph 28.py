import heapq
class Solution:
    def shortestPath(self, edges, n, m, src):
        adj = [[] for _ in range(n)]
        for i,j in edges :
            adj[i].append(j)
            adj[j].append(i)
        dist = [1e9]*n
        parent = [-1]*n
        dist[src] = 0
        queue = []
        queue.append([0,src])
        while queue :
            curr = queue.pop(0)
            distance, node = curr
            for i in adj[node] :
                if distance + 1 < dist[i] :
                    dist[i] = distance + 1
                    queue.append([dist[i],i])
                    parent[i] = node
        for i in range(n) :
            if dist[i]==1e9 :
                dist[i] = -1
        return dist