#include <vector>
#include <unordered_map>
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
    int preorderIndex = 0; 

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int n = inorder.size();
        unordered_map<int, int> inOrderMap;
        inOrderMap.reserve(n);

        for (int i = 0; i < n; i++) {
            inOrderMap.insert(make_pair(inorder[i], i));
        }

        return arrayToTree(0, n - 1, preorder, inorder, inOrderMap);

    }

    TreeNode* arrayToTree(int left, int right, vector<int>& preorder, vector<int>& inorder, unordered_map<int, int>& inOrderMap) {
        if (left > right) {
            return nullptr;
        }

        int rootVal = preorder[preorderIndex];
        TreeNode* root = &TreeNode(rootVal);
        preorderIndex++;

        root->left = arrayToTree(left, inOrderMap[rootVal] - 1, preorder, inorder);
        root->right = arrayToTree(inOrderMap[rootVal] + 1, right, preorder, inorder);

        return root;
    }
};

int main() {

    return 0;
}