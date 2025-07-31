// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/description/

#include <vector>

using namespace std;

class Solution {
public:
    int maximumLength(vector<int>& nums, int k) {
        vector<vector<int>> dp(k, vector<int>(k, 0));
        int ans = 0;
        for (int num : nums) {
            int curr = num % k;
            for (int prev = 0; prev < k; ++prev) {
                dp[curr][prev] = dp[prev][curr] + 1;
                ans = max(ans, dp[curr][prev]);
            }
        }
        return ans;
    }
};