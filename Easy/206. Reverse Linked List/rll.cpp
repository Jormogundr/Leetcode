#include <vector>
#include <iostream>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    // Default ListNodes defined below.
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // If the linked list has no head i.e. is null
        if (head == nullptr) {
            return NULL;
        }

        ListNode* prev = nullptr;
        ListNode* current = head;
        ListNode* next = nullptr;
        while(current != nullptr) {
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        head = prev;
        return head;
    }
};

class SinglyLinkedList {
public:
    ListNode* head;
    SinglyLinkedList() {head = nullptr;} // consturctor, with default value of a null head
    SinglyLinkedList(ListNode* node) {head = node;} // sets the head to the passed ptr

    // Returns the number of nodes in the linked list.
    int listLength() {
        ListNode* temp = head;
        int counter = 0;
        while(temp != nullptr) {
            counter++;
            temp = temp->next;
        }
        return counter;
    }

    // This could be broken up in to two functions, as it currently does two very different things:
    // 1. Print out the contents of the linked list, and 2. return a pointer to an array of values 
    // within the linked list appearing in the same sequence.
    int * getList() {
        int n = listLength();
        int list[n];
        int i = 0;
        ListNode* printnode = head;

        while (printnode != nullptr) {
            cout << printnode->val << " ";
            list[i] = printnode->val;
            printnode = printnode->next;
            i++;
        }
        return list;
    }

   void insert(ListNode* node_to_insert) {
        if (head == nullptr) {
            head = node_to_insert;
            return;
        }

        ListNode* node = head;
        while (node->next != nullptr) {
            ListNode* node = node->next;
        }
        node->next = node_to_insert;
        return;
   }
};

void testCases(){
    int cases[5] = {1,2,3,4,5};
    int output[5] = {5,4,3,2,1};

    // Create the singly linked list which we will reverse
    SinglyLinkedList sll;
    for (int i = 0; i < 5; i++) {
        ListNode node(cases[i], sll.head);
        sll.insert(node);
    } 
    
    Solution solve;
    ListNode* solution = solve.reverseList(sll.head);
    SinglyLinkedList reversed_sll(solution);
    if (reversed_sll.getList() == output) {
        cout << "Success!" << endl;
    }
    else {
        cout << "Failure" << endl;
    }
}

int main() {
    testCases();
    return 0;
}