"""

Given the head of a singly linked list, reverse the list, and return the reversed list.

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""

# Define the node objects. The singly linked list consists of nodes.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# The class the leetcode autograder expects. 
class Solution:

    # Take a singly linked lists and reverses it in place.
    def reverseList(self, head):
        prev = None
        current = head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return self # the leetcode autograde expects a ListNode return type here, so use return self.head.

# This class is used to initialze linked lists from a single ListNode, then generates the singly linked list via the insert() function.
class SinglyLinkedList:
    def __init__(self, head = None):
        self.head = head

    # Traverses list starting with head and prints out val. Prints out the linked list values, and returns a list.
    def printList(self):
        printnode = self.head
        list = []
        while printnode != None:
            print(printnode.val)
            list.append(printnode.val)
            printnode = printnode.next
        return list

    # Inserts node_to_insert at the back of the singly linked list. If the list is empty, set node_to_insert as the head. 
    def insert(self, node_to_insert):
        # Check for empty list, and if empty set the node to the head
        if self.head == None:
            self.head = node_to_insert
            return
        # Instantiate the head so we can traverse the list
        node = self.head
        while node.next != None:
            node = node.next

        # Having traversed the list, add the node at at the back
        node.next = node_to_insert
        return


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def testCases():
    cases = [[1,2],[1,2,3,4,5]]
    output = [[2,1], [5,4,3,2,1]]

    for i,case in enumerate(cases):
        sll = SinglyLinkedList()
        for elem in case:
            node = ListNode(elem)
            sll.insert(node)

        reversed_sll = Solution.reverseList(sll, sll.head)
        if reversed_sll.printList() == output[i]:
            print("Success", case)
        else:
            print("Fail")
    return

def main():
    testCases()

if __name__ == '__main__':
    main()
        