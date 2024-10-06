#include <sstream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  bool areSentencesSimilar(string sentence1, string sentence2) {
    vector<string> s1, s2;
    stringstream ss1(sentence1), ss2(sentence2);
    string word;

    while (ss1 >> word)
      s1.push_back(word);

    while (ss2 >> word)
      s2.push_back(word);

    if (s1.size() == s2.size())
      return s1 == s2;

    if (s2.size() < s1.size()) {
      vector<string> temp = s1;
      s1 = s2;
      s2 = temp;
    }

    int l1 = 0;
    while (l1 < s1.size() && s1[l1] == s2[l1]) {
      l1++;
    }

    int r1 = s1.size() - 1, r2 = s2.size() - 1;
    while (r1 >= l1 && s1[r1] == s2[r2]) {
      r1--;
      r2--;
    }

    return l1 > r1;
  }
};
