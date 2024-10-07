#include <stack>
#include <string>

using namespace std;

class Solution {
public:
  int minLength(string s) {
    stack<char> stack;

    for (char c : s) {

      if (stack.empty()) {
        stack.push(c);
        continue;
      }

      if (c == 'B' && stack.top() == 'A') {
        stack.pop();
        continue;
      }

      if (c == 'D' && stack.top() == 'C') {
        stack.pop();
        continue;
      }

      stack.push(c);
    }

    return stack.size();
  }
};
