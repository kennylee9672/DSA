from graph import Node
from typing import Dict, Set


class Edge:
    def __init__(self, fromNode: Node, toNode: Node, weight: int):
        self.fromNode = fromNode
        self.toNode = toNode
        self.weight = weight


class WeightGraph:
    def __init__(self):
        self.nodes: Dict[str, Node] = {}
        self.adjencencyList: Dict[Node, Set] = {}

    def addNode(self, label: str):
        node = Node(label=label)
        if label not in self.nodes:
            self.nodes[label] = node
        if node not in self.adjencencyList:
            self.adjencencyList[node] = set()

    def addEdge(self, fromLable: str, toLabel: str):
        if fromLable not in self.nodes or toLabel not in self.nodes:
            return
        self.adjencencyList[self.nodes[fromLable]].add(self.nodes[toLabel])

    def print(self):
        for source in self.adjencencyList:
            if self.adjencencyList[source]:
                print(f'{source} is connected to {
                      self.adjencencyList[source]}')

    def __str__(self):
        return f"{str(self.fromNode)}->{str(self.toNode)}"
