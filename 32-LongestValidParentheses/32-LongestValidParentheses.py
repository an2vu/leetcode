# Last updated: 6/3/2026, 6:07:25 PM
1class Solution:
2    def longestValidParentheses(self, s: str) -> int:
3        stack = [-1]
4        max_len = 0
5        for i, ch in enumerate (s):
6            if ch == "(":
7                stack.append(i)
8            else:
9                stack.pop()
10                if not stack :
11                    stack.append(i)
12                else:
13                    max_len = max(max_len, i - stack[-1])
14        return max_len
15