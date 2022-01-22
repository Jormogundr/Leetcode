"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

# Definition for singly-linked list.
from platform import node
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        if head == None or head.next == None:
            return None

        sz = self.getSizeOfLinkedList(head, n)
        nth_node_position = sz - n # position of node to be removed (where the head is position 1)

        count = 1
        curr = head
        while curr != None:
            if count == nth_node_position - 1:
                curr.next = curr.next.next
                return head
            if count == nth_node_position:
                head = curr.next
                return head
            curr = curr.next
            count +=1 

    # Given the head of a linked list and the nth node (from end of list) to remove, determine the position of the nth node and return it as an integer.
    def getSizeOfLinkedList(self, head, n):
        curr = head
        count, sz = 1, 1
        
        while curr != None:
            if count % n == 0:
                count = 1
            count += 1
            sz += 1
            curr = curr.next
        return sz

    # Convert a list to a linked list and return the head. 
    def convertToLinkedList(self, list):
        if len(list) == 0: 
            return None

        node = ListNode(list[0])
        head = node
        for i in range(1, len(list)):
            tmp = ListNode(list[i])
            node.next = tmp 
            node = node.next 
        return head

    # Convert a linked list to a list and return it. 
    def convertToList(self, head):
        if head == None:
            return []

        node = head
        returnList = []
        while node != None:
            returnList.append(node.val)
            node = node.next

        return returnList

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def testCases():
    cases = [([1,2], 2),([1,2,3,4,5], 2), ([1,2], 1), ([1], 1)]
    output = [[2],[1,2,3,5], [1], []]
    for i,case in enumerate(cases):
        head = Solution().convertToLinkedList(case[0]) 
        n = case[1] # the nth node from the back of the list
        solved_ll = Solution().removeNthFromEnd(head, n)
        solved_list = Solution().convertToList(solved_ll)
        if solved_list == output[i]:
            print("Success ", case, solved_list, " == ", output[i])
        else:
            print("Fail ", case, solved_list, " =/= ", output[i])


def main():
    testCases()

if __name__ == '__main__':
    main()