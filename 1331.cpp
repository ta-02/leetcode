
#include <set>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> arrayRankTransform(vector<int> &arr) {
    vector<int> res(arr.size());
    unordered_map<int, int> lookup;
    set<int> sorted_set(arr.begin(), arr.end());

    int rank = 1;
    for (int num : sorted_set) {
      lookup[num] = rank++;
    }

    for (int i = 0; i < arr.size(); i++) {
      res[i] = lookup[arr[i]];
    }

    return res;
  }
};
;
