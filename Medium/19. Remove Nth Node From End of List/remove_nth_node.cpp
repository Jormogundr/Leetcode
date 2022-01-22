#include <vector>
#include <iostream>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    //  # Given the head of a linked list and the nth node (from end of list) to remove, determine the position of the nth node and return it as an integer.
    int getSizeOfLinkedList(ListNode* head, int n) {
        ListNode* curr = head;
        int count = 1;
        int sz = 1;

        while (curr != nullptr) {
            if (count % n == 0) {
                count = 1;
            }
            count += 1;
            sz += 1;
            curr = curr->next;
        }
        return sz;
    }

    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head == nullptr || head->next == nullptr) {
            return nullptr;
        }

        int sz = getSizeOfLinkedList(head, n);
        int nth_node_position = sz - n;
        int count = 1;
        ListNode* curr = head;

        while (curr != nullptr) {
            if (count == nth_node_position - 1) {
                curr->next = curr->next->next;
                return head;
            }
            if (count == nth_node_position) {
                head = curr->next;
                return head;
            }
            curr = curr->next;
            count++;
        }
        return head;
    }
};
