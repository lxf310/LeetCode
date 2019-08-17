//https://leetcode-cn.com/problems/word-search

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        for (int i = 0; i< board.size(); ++ i) {
            for (int j = 0; j < board[0].size(); ++ j) {
                if (this->dfs(board, i, j, word, 0)) {
                    return true;
                }
            }
        }
        return false;
    }
    
    
    bool dfs(vector<vector<char>>& board, int i, int j, string& word, int curLen) {
        if (curLen == word.size()) {
            return true;
        }
        if (i < 0 || j < 0 || i >= board.size() || j >= board[0].size() || board[i][j] != word[curLen]) {
            return false;
        }
        char tmp = board[i][j];
        board[i][j] = '*';
        bool res = (this->dfs(board, i+1, j, word, curLen+1) ||
                    this->dfs(board, i, j+1, word, curLen+1) ||
                    this->dfs(board, i-1, j, word, curLen+1) ||
                    this->dfs(board, i, j-1, word, curLen+1));
        board[i][j] = tmp;
        return res;
    }
};
