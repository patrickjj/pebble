import collections
import random

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = collections.defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printGraph(self):
        for i in range(self.V):
            for j in self.graph[i]:
                print(f"{i} ---> {j}", end="\t")
            print()

    def generateRandomGraph(self, num_nodes, num_edges):
        self.V = num_nodes
        self.graph = collections.defaultdict(list)
        for i in range(num_edges):
            u = random.randint(0, num_nodes-1)
            v = random.randint(0, num_nodes-1)
            self.addEdge(u, v)

    def BFS(self, s, t):
        begin = s
        queue = collections.deque()
        queue.append(s)
        visited = [False] * (self.V)
        visited[s] = True
        nodes_visited = 0

        while queue:
            s = queue.popleft()
            nodes_visited += 1
            if s == t:
                print(f"BFS: Found path from {begin} to {t}. Visited {nodes_visited} nodes.")
                return True
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        print(f"BFS: No path from {begin} to {t}. Visited {nodes_visited} nodes.")
        return False

    def DFS(self, s, t):
        begin = s
        stack = [s]
        visited = [False] * (self.V)
        visited[s] = True
        nodes_visited = 0

        while stack:
            s = stack.pop()
            nodes_visited += 1
            if s == t:
                print(f"DFS: Found path from {begin} to {t}. Visited {nodes_visited} nodes.")
                return True
            for i in self.graph[s][::-1]:
                if visited[i] == False:
                    stack.append(i)
                    visited[i] = True
        print(f"DFS: No path from {begin} to {t}. Visited {nodes_visited} nodes.")
        return False

def main():
    graph = Graph(100)
    graph.generateRandomGraph(100, 1000)
    graph.printGraph()

    s = 0
    t = 99
    graph.BFS(s, t)
    graph.DFS(s, t)

if __name__ == '__main__':
    main()
