// https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int start = 0;
        int end = 0;
        int max = 0;
        for (int i = 0; i < s.size(); ++i) {
            for (end = start; end < i; ++ end) {
                if (s[end] == s[i]) {
                    start = end + 1;
                    break;
                }
            }
            if (end - start + 1 > max) {
                max = end - start + 1;
            }
        }
        return max;
    }
};

/*
 * "bbb!ba"
 */
