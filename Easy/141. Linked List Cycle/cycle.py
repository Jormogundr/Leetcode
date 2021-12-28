""""

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Constraints:

The number of the nodes in the list is in the range [0, 104].
-10E5 <= Node.val <= 10E5
pos is -1 or a valid index in the linked-list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # This brute force method depends on traversing the entire linked list and using the constraint for the maximum
    # number of nodes to determine if we are stuck in a loop or not. Rather inefficient. Ran in the autograder in 192 ms
    # compare that to the same implementation in C++, at 12 ms!
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        
        node = head
        max = 10E4
        count = 0
        while node.next != None:
            if count > max:
                return True
            count += 1
            node = node.next
        return False

    # This solution posted in the discussion is clever: it relies on the 'fast' pointer catching up to the 
    # 'slow' pointer IF there is a loop in the list.
    def hasCycle(self, head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False