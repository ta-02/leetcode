#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  bool canArrange(vector<int> &arr, int k) {
    unordered_map<int, int> f;

    for (int n : arr) {
      int rem = ((n % k) + k) % k;
      f[rem]++;
    }

    for (auto [key, other] : f) {
      int other_key = (k - key) % k;

      if (other_key == key && f[key] % 2 != 0)
        return false;

      if (f[other_key] != f[key])
        return false;
    }

    return true;
  }
};
