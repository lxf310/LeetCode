/// https://leetcode-cn.com/problems/validate-binary-search-tree/

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
    // my own solution
    bool isValidBST_WithAssistance(TreeNode* root) {
        return  ((root == NULL) ||
        (this->less(root, root->left) && this->isValidBST(root->left)) &&
        (this->larger(root, root->right) && this->isValidBST(root->right)));
    }
    
    bool less(TreeNode* root, TreeNode* child) {
        return (child == NULL ||
                root->val > child->val &&
                this->less(root, child->left) &&
                this->less(root, child->right));
    }
    
    bool larger(TreeNode* root, TreeNode* child) {
        return (child == NULL ||
                root->val < child->val &&
                this->larger(root, child->left) &&
                this->larger(root, child->right));
    }
    
    // reference solution
    bool isValidBST(TreeNode* root, long long min = LONG_LONG_MIN, long long max = LONG_LONG_MAX) {
        if (root == NULL) {
            return true;
        }
        
        if (root->val <= min || root->val >= max) {
            return false;
        }
        
        return isValidBST(root->left, min, root->val) && isValidBST(root->right, root->val, max);
    }
};
