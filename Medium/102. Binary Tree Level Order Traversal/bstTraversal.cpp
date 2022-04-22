#include <vector> 
using namespace std;


// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> levelOrder;
        if (root == nullptr) {
            return levelOrder;
        }
        levelOrder = {{root->val}};
        vector<TreeNode*> queue {root};
        vector<int> levelList;

        while (!queue.empty()) {
            int size = queue.size();
            levelList = {};
            while (size > 0) {
                TreeNode* temp = queue[0];
                queue.erase(queue.begin());
                if (temp->left != nullptr) {
                    levelList.insert(levelList.end(), temp->left->val);
                    queue.insert(queue.end(), temp->left);
                }
                if (temp->right != nullptr) {
                    levelList.insert(levelList.end(), temp->right->val);
                    queue.insert(queue.end(), temp->right);
                }
                size--;
            }
        if (!levelList.empty()) {
            levelOrder.insert(levelOrder.end(), levelList);
        }
        }
        return levelOrder;
    }
};