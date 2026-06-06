# Last updated: 22:55:18 6/6/2026
1class Solution:
2    def minimumTotal(self, triangle: List[List[int]]) -> int:
3        dp = [0] * (len(triangle) + 1)
4        for row in triangle[::-1]:
5            for i, n  in enumerate(row) :
6                dp[i] = min ((dp[i] + row[i]), (dp[i+1] + row[i]))
7        return dp[0]
8                