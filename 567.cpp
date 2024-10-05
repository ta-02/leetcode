#include <map>
#include <string>
using namespace std;

class Solution {
public:
  bool checkInclusion(string s1, string s2) {
    int w = s1.size();
    int n = s2.size();
    if (w > n)
      return false;

    map<char, int> f1, f2;

    for (char c : s1)
      f1[c]++;

    for (int i = 0; i < w; i++)
      f2[s2[i]]++;

    for (int i = w; i < n; i++) {
      if (f1 == f2)
        return true;

      f2[s2[i - w]]--;
      if (f2[s2[i - w]] == 0)
        f2.erase(s2[i - w]);

      f2[s2[i]]++;
    }

    return f1 == f2;
  }
};
