#include <string>

using namespace std;

class Solution {
public:
  int minAddToMakeValid(string s) {
    int lbrac, rbrac = 0;
    for (char c : s) {
      if (c == '(')
        lbrac++;
      else
        rbrac++;
    }

    int b, sm;
    if (lbrac > rbrac) {
      b = lbrac;
      sm = rbrac;
    } else {
      b = rbrac;
      sm = lbrac;
    }

    return (b - sm);
  }
};
