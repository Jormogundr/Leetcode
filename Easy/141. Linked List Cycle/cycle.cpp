/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == nullptr) {
            return false;
        }
        
        ListNode* node = head;
        int max = 10E4;
        int count = 0;
        
        while (node->next != nullptr) {
            if (count > max) {
                return true;
            }
            count++;
            node = node->next;
        }
        return false;
    }
};