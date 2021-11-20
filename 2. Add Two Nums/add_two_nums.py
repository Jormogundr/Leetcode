# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Traverses list starting with head and prints out val
    def printList(self):
        printvalue = self.head
        
        while printvalue != None:
            print(printvalue.val)
            printvalue = printvalue.next

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
        
class Solution:
    def addTwoNumbers(self, l1, l2):

        def createLinkedLists(l1, l2):
            list1 = SinglyLinkedList()
            list2 = SinglyLinkedList()
            for i, j in zip(l1,l2):
                node1 = ListNode(i)
                node2 = ListNode(j)
                list1.insert(node1)
                list2.insert(node2)
            return list1, list2

        ll1, ll2 = createLinkedLists(l1, l2)
        ll3 = SinglyLinkedList()
        node1 = ll1.head
        node2 = ll2.head
        # Currently assumes both linked lists are equal in length
        while node1 != None and node2 != None:
            node3 = ListNode(node1.val + node2.val)
            node1 = node1.next
            node2 = node2.next
            ll3.insert(node3)
        return ll3

        

        
if __name__ == '__main__': # if this file is explicitly run
    
    # Create lists to reintrepret into linked lists
    l1 = [2,4,3]
    l2 = [5,6,4]
    list3 = Solution().addTwoNumbers(l1, l2)
    list3.printList()
