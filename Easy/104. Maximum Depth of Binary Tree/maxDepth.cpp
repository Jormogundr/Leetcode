#include <vector>

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
    int maxDepth(TreeNode* root) {
        if (not root) { return 0; }

        int depth = 0;
        std::vector<TreeNode*> queue;
        queue.push_back(root);

        while (!queue.empty()) {
            int size = queue.size();
            while (size > 0) {
                TreeNode *temp = queue.front();
                queue.erase(queue.begin());
                if (temp->left != nullptr) {queue.push_back(temp->left);}
                if (temp->right != nullptr) {queue.push_back(temp->right);}
                size--;
            }
        depth++;
        }
    return depth;
    }
};