// https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal_recursion(TreeNode* root) {
        vector<int> ret;
        this->traversal(root, ret);
        return ret;
    }
    
    void traversal(TreeNode* root, vector<int>& ret) {
        if (root != NULL) {
            this->traversal(root->left, ret);
            ret.push_back(root->val);
            this->traversal(root->right, ret);
        }
    }
    
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ret;
        if (root == NULL) {
            return ret;
        }
        stack<TreeNode*> nodes;
        while (root) {
            nodes.push(root);
            root = root->left;
        }
        while (nodes.size() > 0) {
            root = nodes.top();
            nodes.pop();
            ret.push_back(root->val);
            if (root->right) {
                root = root->right;
                nodes.push(root);
                while (root->left) {
                    root = root->left;
                    nodes.push(root);
                }
            }
        }
        return ret;
    }
};
