/// https://leetcode-cn.com/problems/unique-binary-search-trees/
/*
* G(n) => the number of BST with n nodes
* f(n) => the number of BST with n nodes and the root node equals n
* G(n) = f(1) + f(2) + ... + f(n)
* f(i) = G(i-1)*G(n-i)
* 
* G(i) = G(1-1)*G(n-1) + G(2-1)*G(n-2) + ... + G(j-1)*G(i-j)
*/
class Solution {
public:
    int numTrees(int n) {
        vector<int> dp(n+1, 0);
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i <= n; ++ i) {
            for (int j = 1; j <= i; ++ j) {
                dp[i] += dp[j-1] * dp[i-j];
            }
        }
        return dp[n];
    }
};
