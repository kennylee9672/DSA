# from lib.node.graph_node import Node
from typing import Dict, Set


class Node:
    def __init__(self, label):
        self.label = label

    def print(self):
        print(self.label)

    def __repr__(self):
        return str(self.label)

    def __str__(self):
        return str(self.label)


class Graph:
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

    def removeNode(self, label):
        if label not in self.nodes:
            return

        for source in self.adjencencyList:
            if self.nodes[label] not in self.adjencencyList[source]:
                continue
            self.adjencencyList[source].remove(self.nodes[label])
        self.adjencencyList.pop(self.nodes[label])
        self.nodes.pop(label)

    def removeEdge(self, fromLable, toLable):
        if not self.ifExists(fromLable, toLable):
            return

        self.adjencencyList[self.nodes[fromLable]].remove(self.nodes[toLable])

    def ifExists(self, fromLable, toLable):
        return fromLable in self.nodes and toLable in self.nodes


if __name__ == "__main__":
    print('Kenny')
    graph = Graph()
    for lable in ["A", "B", "C", "D", "E"]:
        graph.addNode(lable)
    graph.addEdge("A", "B")
    graph.addEdge("A", "C")
    graph.removeEdge("A", "B")
    graph.removeNode("A")
    graph.print()
