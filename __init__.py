from lib.binary_search_tree import BinarySearchTree
from tests import (
    testTraveral,
    testProperties,
    testEquality,
    testValidBST,
    testBFS,
)

if __name__ == "__main__":
    # testTraveral()
    # testProperties()
    # testEquality()

    # tree = BinarySearchTree()
    # for x in [20, 10, 30]:
    #     tree.insert(x)
    # testValidBST(tree=tree)
    
    testBFS()


'''
    20
10     30
         40


v.20
    -> v.20.left=10
        -> v.10.left=N
            <- N
        -> v.10.right=N
            <- N
        <= ap(10)
    -> v.20.right=30
        -> v.30.left=N
            <- N
        -> v.30.right=40
            -> v.40.left=N
                <- N
            -> v.40.right=N
                <- N
            <= ap(40)
        <= ap(30)
    <= ap(20)

Append Order: 10, 40, 30, 20
Call Sequesnce: 20 -> 10 -> 30 -> 40
'''


'''
        20
   10        30
 6    14  24
3 8          26
'''