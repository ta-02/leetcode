from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
      res = []
      path = []
      N = len(s)

      def dfs(i):
        if i >= N:
          res.append(path[:])
          return  
        for j in range(i, N):
          if s[i:j+1] == s[i:j+1][::-1]:
            path.append(s[i:j+1])
            dfs(j+1)
            path.pop()
            
      dfs(0)
      return res


        
            


        
            
