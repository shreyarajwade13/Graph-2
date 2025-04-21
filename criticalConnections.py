"""
Graph DFS approach -
TC = O(V + E)
SC = O(V + E) ==> we are using discovery O(n), lowest array O(n),
AND list/hashmap to keep track of vertices and their child O(V + E)
but since O(V + E) dominates, that's the final SC
"""


class Solution:
    def __init__(self):
        self.time = 0

    def getGraph(self, n, connections):
        adjList = []

        # create n empty lists in adjList
        for i in range(n):
            adjList.append([])

        for edge in connections:
            _from = edge[0]
            to = edge[1]
            adjList[_from].append(to)
            adjList[to].append(_from)
        return adjList

    # parent ==> u
    def dfs(self, graph, discovery, lowest, v, parent, rtnData):
        # base
        if discovery[v] != -1: return

        # logic
        discovery[v] = self.time
        lowest[v] = self.time
        self.time += 1

        # child_v ==> n ==> child of v
        for child_v in graph[v]:
            if child_v == parent: continue

            if discovery[child_v] == -1:
                # Recurse into the neighbor
                self.dfs(graph, discovery, lowest, child_v, v, rtnData)

                # if dfs comes to end i.e. last child node eg. 2 --> 4 --> 2
                if lowest[child_v] > discovery[v]:
                    rtnData.append([child_v, v])
                # Update the lowest reachable time for the current node
                lowest[v] = min(lowest[v], lowest[child_v])
            else:
                # Update the lowest time for the current node if a back edge exists
                lowest[v] = min(lowest[v], lowest[child_v])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        if n is None or len(connections) == 0: return []

        rtnData = []

        discovery = [-1] * n
        lowest = [-1] * n

        # step 1: create graph/adjList
        graph = self.getGraph(n, connections)
        # print(graph)

        # step 2: call dfs
        # 0 ==> v ==> child
        # -1 ==> u ==> parent of child
        self.dfs(graph, discovery, lowest, 0, -1, rtnData)

        return rtnData