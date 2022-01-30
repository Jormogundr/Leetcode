#include <limits>
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
    bool isValidBST(TreeNode* root, double min = -numeric_limits<double>::infinity(), double max = numeric_limits<double>::infinity()) {
        if (not root) {
            return true;
        }
        if (root->val <= min or root->val >= max) {
            return false;
        }
        else {
            return isValidBST(root->left, min, root->val) and isValidBST(root->right, root->val, max);
        }
    }
};