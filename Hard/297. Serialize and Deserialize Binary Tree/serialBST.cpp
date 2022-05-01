#include <vector>
#include <string>
#include <queue>
#include <iostream>
using namespace std;


// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (root == NULL) {
            return "";
        }
        string treeToString = to_string(root->val);
        treeToString.append(",");
        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            TreeNode* temp = q.front();
            q.pop();
            vector<TreeNode*> children {temp->left, temp->right};

            for (TreeNode* child : children) {
                if (child) {
                    q.push(child);
                    string value = to_string(child->val);
                    value += ",";
                    treeToString += value;
                }
                else {
                    treeToString += "None,";
                }
            }
        }

        return treeToString;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data.length() == 0) return nullptr;
        int pos = 0;
        vector<string> dataToList;
        string token;

        // Convert string delimited by "," to a vector of strings
        // See program 4 here https://www.javatpoint.com/how-to-split-strings-in-cpp
        while ((pos = data.find(",")) < data.size()) {
            token = data.substr(0, pos);
            dataToList.push_back(token);
            data.erase(0, pos + 1);
        }
        
        int n = dataToList.size();
        if (n <= 1) return nullptr;
        TreeNode* root = new TreeNode(stoi(dataToList[0]));
        queue<TreeNode*> q;
        q.push(root);
        int i = 1; int val;
        TreeNode* temp;

        while (i < n && !q.empty()) {
            temp = q.front();
            q.pop();
            if (dataToList[i] != "None") {
                val = stoi(dataToList[i]);
                temp->left = new TreeNode(val);
                q.push(temp->left);
            } 
            i++;

            if (i < n && dataToList[i] != "None") {
                val = stoi(dataToList[i]);
                temp->right = new TreeNode(val);
                q.push(temp->right);
            }
            i++;
        }
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));


int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->right->left = new TreeNode(4);
    root->right->right = new TreeNode(5);

    Codec solution;
    string ser = solution.serialize(root);
    TreeNode* deser = solution.deserialize(ser);

    return 0;
}