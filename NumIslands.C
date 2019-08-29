// https://leetcode-cn.com/problems/number-of-islands/

/* It means to traverse the graph */
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++ j) {
                if (grid[i][j] == '1') {
                    ++ count;
                    dfsMark(i, j, grid);
                }
            }
        }
        return count;
    }
    
    void dfsMark(int i, int j, vector<vector<char>>& grid) {
        grid[i][j] = 'v';
        // up
        if (validArea(i-1, j, grid) && grid[i-1][j] == '1') {
            dfsMark(i-1, j, grid);
        }
        // down
        if (validArea(i+1, j, grid) && grid[i+1][j] == '1') {
            dfsMark(i+1, j, grid);
        }
        // left
        if (validArea(i, j-1, grid) && grid[i][j-1] == '1') {
            dfsMark(i, j-1, grid);
        }
        // right
        if (validArea(i, j+1, grid) && grid[i][j+1] == '1') {
            dfsMark(i, j+1, grid);
        }
    }
    
    bool validArea(int i, int j, vector<vector<char>>& grid) {
        return (i >= 0 && i < grid.size() && j >= 0 && j < grid[0].size());
    }
    
    /* out of time limitation */
    void bfsMark(int i, int j, vector<vector<char>>& grid) {
        queue<vector<int>> myQueue;
        int directions[4][2] = {{-1,0}, {1,0}, {0,-1}, {0,1}};
        
        vector<int> tmp;
        tmp.push_back(i);
        tmp.push_back(j);
        myQueue.push(tmp);
        
        while (!myQueue.empty()) {
            vector<int> node = myQueue.front();
            grid[node[0]][node[1]] = 'v';
            myQueue.pop();
            for (int k = 0; k < 4; ++ k) {
                int ki = node[0] + directions[k][0];
                int kj = node[1] + directions[k][1];
                if (validArea(ki, kj, grid) && grid[ki][kj] == '1') {
                    vector<int> tmp;
                    tmp.push_back(ki);
                    tmp.push_back(kj);
                    myQueue.push(tmp);
                }
            }
        }
    }
};
