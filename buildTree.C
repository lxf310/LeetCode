// https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return buildTree(0, preorder.size()-1, preorder, 0, inorder.size()-1, inorder);
    }
    
    TreeNode* buildTree(int pre_s, int pre_e, vector<int>& preorder, int in_s, int in_e, vector<int>& inorder) {
        TreeNode *root = NULL;
        // cout << pre_s << "," << pre_e << "," << in_s << "," << in_e << endl;
        if (pre_s <= pre_e && in_s <= in_e) {
            root = new TreeNode(preorder[pre_s]);
            // The root position in inorder list
            int in_root = in_s;
            while (in_root <= in_e and inorder[in_root] != preorder[pre_s]) {
                ++ in_root;
            }
            int left_length = in_root - in_s;
            root->left = buildTree(pre_s+1, pre_s+left_length, preorder, in_s, in_root-1, inorder);
            root->right = buildTree(pre_s+left_length+1, pre_e, preorder, in_root+1, in_e, inorder);
        }
        return root;
    }
};
