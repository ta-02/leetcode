#include <vector>

using namespace std;

class Solution {
public:
  int maxSubArray(vector<int> &nums) {
    int best = nums[0], sum = nums[0];

    for (int i = 1; i < nums.size(); i++) {
      sum = max(nums[i], sum + nums[i]);
      best = max(sum, best);
    }

    return best;
  }
};
