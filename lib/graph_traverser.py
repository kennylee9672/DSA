from lib.graph import Graph, Node
from typing import Set


class Traverser:
    def __init__(self, graph: Graph):
        self.adj = graph.adjencencyList
        self.nodes = graph.nodes

    # 'A' -> 'B'
    def depthFirstSearchAt(self, root: str):
        if root not in self.nodes:
            return

        result = []

        def _dfs(n: Node, visited: Set):
            # visited.add(n)
            result.append(n.label)
            for nb in self.adj[n]:
                if nb not in visited:
                    visited.add(nb)
                    _dfs(nb, visited)

        _dfs(self.nodes[root], set())
        print(result)

    def depthFirstSearchIterAt(self, root: str):
        if root not in self.nodes:
            return

        result = []
        visited = set()
        q = [self.nodes[root]]
        while q:
            curr = q.pop(-1)
            result.append(curr.label)

            for nb in self.adj[curr]:
                if nb not in visited:
                    visited.add(nb)
                    q.append(nb)
        print(result)

    def breathFirstSearch(self, root: str):
        if root not in self.nodes:
            return

        result = []
        visited = set()
        q = [self.nodes[root]]
        while q:
            curr = q.pop(0)
            result.append(curr.label)

            for nb in self.adj[curr]:
                if nb not in visited:
                    visited.add(nb)
                    q.append(nb)
        print(result)

    def topologicalSort(self):
        def _sort(n: Node):
            if n in visited:
                return

            visited.add(n)
            for nb in self.adj[n]:
                _sort(nb)
            q.append(n)

        visited = set()
        q = []

        for n in self.adj:
            _sort(n)

        sorted_list = []
        while q:
            sorted_list.append(q.pop().label)
        print(sorted_list)
        return sorted_list

    def hasCycle(self) -> bool:
        def dfs(n: Node):
            visiting.add(n)

            for nb in self.adj[n]:
                if nb in visited:
                    continue
                if nb in visiting:
                    return True
                if dfs(nb):
                    return True

            visiting.remove(n)
            visited.add(n)

            return False

        visited = set()
        visiting = set()
        for n in self.adj:
            if n not in visited and dfs(n):
                return True
        return False
