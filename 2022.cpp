#include <vector>

using namespace std;

class Solution {
public:
  vector<vector<int>> construct2DArray(vector<int> &original, int m, int n) {
    vector<vector<int>> res(m, vector<int>(n));

    vector<vector<int>> res2(m, vector<int>(n));

    if (original.size() != m * n) {
      return {};
    }

    int index = 0;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        res[i][j] = original[index++];
      }
    }

    return res;
  }
};
