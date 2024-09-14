#include <vector>

using namespace std;

class Solution {
public:
  int longestSubarray(vector<int> &nums) {
    int size, res, currMax = 0;

    for (int n : nums) {
      if (n > currMax) {
        currMax = n;
        size = 1;
        res = 0;
      } else if (n == currMax) {
        size++;
      } else {
        size = 0;
      }
      res = max(res, size);
    }

    return res;
  }
};
