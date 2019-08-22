// https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int size = prices.size();
        if (size == 0) {
            return 0;
        }
        // The action taken by the ith day has three choices
        vector<int> sell(size, 0);
        vector<int> buy(size, 0);
        vector<int> cool(size, 0);
        buy[0] = -prices[0];
        for (int i = 1; i < size; ++ i) {
            sell[i] = max(sell[i-1], buy[i-1]+prices[i]);
            // The action taken by the day before buying must be cooldown
            buy[i] = max(buy[i-1], cool[i-1]-prices[i]);
            cool[i] = max(max(cool[i-1], buy[i-1]), sell[i-1]);
        }
        return sell[size-1];
    }
};
