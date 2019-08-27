// https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
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
    void flatten_recursion(TreeNode* root) {
        if (root != NULL) {
            flatten(root->left);
            flatten(root->right);
            TreeNode* right = root->right;
            root->right = root->left;
            root->left = NULL;
            TreeNode* p = root;
            while (p->right != NULL) {
                p = p->right;
            }
            p->right = right;
        }
    }
    
    void flatten(TreeNode* root) {
        stack<TreeNode*> nodes;
        TreeNode* p = root;
        while (p != NULL || !nodes.empty()) {
            while (p != NULL) {
                nodes.push(p);
                p = p->left;
            }
            
            if (!nodes.empty()) {
                p = nodes.top();
                nodes.pop();
                TreeNode* r = p->right;
                p->right = p->left;
                p->left = NULL;
                
                while (p->right != NULL) {
                    p = p->right;
                }
                p->right = r;
                p = r;
            }
        }
    }
};
