from lib.binary_search_tree import BinarySearchTree
from lib.tree_traveral import Traverser


example = BinarySearchTree()
for x in [20, 10, 30, 6, 14, 24, 3, 8, 26]:
    example.insert(x)


def testTraveral(tree=example):
    print('PreOrder: ', Traverser(tree).preOrder())
    print('InOrder: ', Traverser(tree).inOrder())

    treePost = BinarySearchTree()
    for x in [20, 10, 30]:
        treePost.insert(x)
    print('PostOrder: ', Traverser(tree).postOrder())
    print('BFS: ', Traverser(tree).breadthFirstSearch())
    print()


def testProperties(tree=example):
    print('Height: ', Traverser(tree).height())
    print('MinNode: ', Traverser(tree).minNode())
    print()


def testEquality(tree=example):
    tree_diff = BinarySearchTree()
    for x in [20, 10, 30, 6, 14, 24, 3, 8]:
        tree_diff.insert(x)
    print('Equals with Identical: ', Traverser(tree).equals(tree))
    print('Equals with Diff: ', Traverser(tree).equals(tree_diff))
    print('Equals with None: ', Traverser(tree).equals(None))
    print()


def testValidBST(tree=example):
    print('Valid BST: ', Traverser(tree).validBST())
    tvr = Traverser(tree)
    tvr.swap()
    print('Valid BST with swap: ', tvr.validBST())
    print()


def testBFS(tree=example):
    print('BFS: ', Traverser(tree).BFS())
    print()
    
