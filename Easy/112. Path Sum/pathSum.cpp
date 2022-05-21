
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
    bool hasPathSum(TreeNode* root, int targetSum) {
        setTargetSum(targetSum);
        if (root == nullptr) {return false;}
        bool hasValidPath = dfs(root, 0);
        if (hasValidPath) {return true;}
        else {return false;}

    }

    bool dfs(TreeNode *node, int sum) {
        if (node != nullptr) {
            sum += node->val;
            if (node->left == nullptr && node->right == nullptr) {return sum == getTargetSum();}
            if (dfs(node->right, sum) || dfs(node->left, sum)) {return true;}
            else {return false;}
        }
        else {return false;}
    }

    int getTargetSum() {return targetSum_;}
    void setTargetSum(int s) {targetSum_ = s;}
    int targetSum_;
};