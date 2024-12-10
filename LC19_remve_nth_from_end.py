'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''

from lib.linked_list import Node, LinkedList


def removeNthFromEnd(nums: LinkedList, k):
    dummy = Node(-1)
    dummy.next = nums.first

    i, j = nums.first, nums.first
    for _ in range(k - 1):
        j = j.next
    
    prev = dummy
    while j.next:
        prev = i
        i = i.next
        j = j.next

    prev.next = i.next
    i.next = None
    if prev.val == -1:
        nums.first = prev.next


if __name__ == "__main__":
    # [10]
    nums = LinkedList()
    nums.addLast(10)
    removeNthFromEnd(nums, 1)
    nums.print()
    
    # expect [10]
    nums = LinkedList()
    nums.addLast(10)
    nums.addLast(20)
    removeNthFromEnd(nums, 1)
    nums.print()
    
    # expect [20]
    nums = LinkedList()
    nums.addLast(10)
    nums.addLast(20)
    removeNthFromEnd(nums, 2)
    nums.print()
    
    # nums.addLast(20)
    # nums.addLast(30)
    # nums.addLast(40)
    # nums.addLast(50)