# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

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
    def mergeTwoLists(self, l1, l2):

        def createLinkedLists(l1, l2):
            list1 = SinglyLinkedList()
            list2 = SinglyLinkedList()
            for i, j in zip(l1,l2):
                node1 = ListNode(i)
                node2 = ListNode(j)
                list1.insert(node1)
                list2.insert(node2)
            return list1, list2

    return list


        

        
if __name__ == '__main__': # if this file is explicitly run
    
    # Create lists to reintrepret into linked lists
    l1 = [1,2,4]
    l2 = [1,3,4]
    list3 = Solution().mergeTwoLists(l1, l2)
    list3.printList()
