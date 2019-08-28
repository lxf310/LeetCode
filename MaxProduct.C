// https://leetcode-cn.com/problems/maximum-product-subarray/

/* 
* Analysis:
* To end with nums[i], nums[i] must be included by the current result.
* Regardless nums[i] is postive or negative, the current max result is the max value among nums[i], lastMax*nums[i] and lastMin*nums[i].
* The current min comes from them as well.
* Key point is: neg*neg and pos*pos are pos; neg*pos is neg.
*/
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int mi = nums[0];
        int ma = mi;
        int ret = mi;
        for (int i = 1; i< nums.size(); ++ i) {
            int tmp = ma; // store lastMax into tmp.
            ma = max(nums[i], max(nums[i]*ma, nums[i]*mi));
            mi = min(nums[i], min(nums[i]*tmp, nums[i]*mi));
            ret = max(ma, ret);
        }
        return ret;
    }
};
