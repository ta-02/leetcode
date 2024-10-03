#include <numeric>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  int minSubarray(vector<int> &nums, int p) {
    int n = nums.size(), totalSum = 0;

    for (int num : nums) {
      totalSum = (totalSum + num) % p;
    }

    int target = totalSum % p;
    if (target == 0)
      return 0;

    unordered_map<int, int> mp;
    mp[0] = -1;

    int currSum = 0, minLen = n;

    for (int i = 0; i < n; ++i) {
      currSum = (currSum + nums[i]) % p;
      int needed = (currSum - target + p) % p;

      if (mp.find(needed) != mp.end()) {
        minLen = min(minLen, i - mp[needed]);
      }

      mp[currSum] = i;
    }

    return minLen == n ? -1 : minLen;
  }
};
