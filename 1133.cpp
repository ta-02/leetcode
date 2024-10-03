#include <map>
#include <vector>

using namespace std;

class Solution {
public:
  int largestUniqueNumber(vector<int> &nums) {
    int res = -1;
    map<int, int> mp;

    for (int n : nums) {
      mp[n]++;
    }

    for (auto [k, v] : mp) {
      if (v == 1)
        res = max(res, k);
    }

    return res;
  }
};
