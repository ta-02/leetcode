#include <set>
#include <vector>

using namespace std;
class Solution {
public:
  int countConsistentStrings(string allowed, vector<string> &words) {
    int res = 0;

    set<int> freq;
    for (char c : allowed) {
      freq.insert(c);
    }

    for (string word : words) {
      bool has_all = true;
      for (char c : word) {
        if (freq.count(c) == 0) {
          has_all = false;
          break;
        }
      }
      if (has_all) {
        res++;
      }
    }

    return res;
  }
};
