#include <numeric>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  long long dividePlayers(vector<int> &skill) {
    int n = skill.size();
    int np = n / 2;
    long long res = 0;
    int total = accumulate(skill.begin(), skill.end(), 0);

    if (total % np != 0) {
      return -1;
    }

    int s_pt = total / np;

    unordered_map<int, int> f;
    for (int n : skill) {
      f[n]++;
    }

    for (int i = 0; i < skill.size(); ++i) {
      if (f[skill[i]] == 0) {
        continue;
      }

      int complement = s_pt - skill[i];
      if (f[complement] == 0) {
        return -1;
      }

      if (complement == skill[i] && f[complement] < 2) {
        return -1;
      }

      f[skill[i]]--;
      f[complement]--;
      res += (complement * skill[i]);
    }

    return res;
  }
};
