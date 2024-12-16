from lib.binary_search_tree import BinarySearchTree
from lib.graph_traverser import Traverser
from lib.graph import Graph
from tests import (
    testTraveral,
    testProperties,
    testEquality,
    testValidBST,
    testBFS,
)


def createGraph():
    graph = Graph()
    for lable in ["A", "B", "C", "D"]:
        graph.addNode(lable)
    graph.addEdge("A", "B")
    graph.addEdge("B", "D")
    graph.addEdge("D", "C")
    graph.addEdge("A", "C")
    # graph.print()
    return graph


def createGraph2():
    graph = Graph()
    for lable in ["A", "B", "C", "D", "E"]:
        graph.addNode(lable)
    graph.addEdge("A", "B")
    graph.addEdge("A", "E")
    graph.addEdge("B", "E")
    graph.addEdge("C", "A")
    graph.addEdge("C", "B")
    graph.addEdge("C", "D")
    graph.addEdge("D", "E")
    # graph.print()
    return graph


def createTopoGraph():
    graph = Graph()
    for lable in ["X", "A", "B", "P"]:
        graph.addNode(lable)
    graph.addEdge("X", "A")
    graph.addEdge("X", "B")
    graph.addEdge("A", "P")
    graph.addEdge("B", "P")
    # graph.print()
    return graph


def createCycle():
    graph = Graph()
    for lable in ["A", "B", "C"]:
        graph.addNode(lable)
    graph.addEdge("A", "B")
    graph.addEdge("B", "C")
    graph.addEdge("A", "C")
    # graph.print()
    return graph


'''
   A -> B
 <|     |>
C    <-    D
'''
if __name__ == "__main__":
    graph = createCycle()
    traverser = Traverser(graph)
    traverser.depthFirstSearchAt("A")
    traverser.depthFirstSearchIterAt("A")
    traverser.breathFirstSearch("A")
    traverser.topologicalSort()
    print(traverser.hasCycle())


# testTraveral()
# testProperties()
# testEquality()

# tree = BinarySearchTree()
# for x in [20, 10, 30]:
#     tree.insert(x)
# testValidBST(tree=tree)

# testBFS()
